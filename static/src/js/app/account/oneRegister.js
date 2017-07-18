var choose = $('.chooseleft');
var loginYes = $('.loginYes');
var loginNo = $('.loginNo');

choose.click(function(){
        loginYes.toggle();
	    loginNo.toggle();
	})


$('#captcha-img').click(function(){
        $("#captcha-img")[0].src = "/captcha/?" + Math.random();
        $("#captcha")[0].value = "";
});


$("form").on("submit", function(){
	var phone = $("#phone").val();
	var captcha = $("#captcha").val();

    var phoneReg = /^(((1[0-9]{2}))+\d{8})$/;
    if(!phoneReg.test($("#phone").val()))
    {
        $("#error-info").empty();
        $("#error-info").append("请输入有效的手机号码");
        return false;
    }
    else{
        $.ajax({
            beforeSend: csrfTokenHeader,
            url: "/MessageAPIView/",
            async: false,
            data: {phone: phone, captcha: captcha, pageState: 0},
            dataType: "json",
            type: "GET",
            success: function (data) {
                console.log(data.code);
                if(!data.code) {
                    console.log(data.data)
                    window.location.href = "/twoRegister/";
                }
                else{
                    $("#error-info").empty();
                    $("#error-info").append(data.data);
                    $("#captcha-img")[0].src = "/captcha/?" + Math.random();
                    $("#captcha")[0].value = "";
                }
            },
            error: function (){
                alert("错误");
            }
        });
    }
	return false;
});

