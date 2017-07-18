var detaLi = $('.detaLi');
var dataInput = $('#dataInput');
var chooseleft = $('#chooseleft');
var showChoose = $('#showChoose');
console.log(detaLi);
//选择金额
detaLi.click(function(){
	var val = $(this).text().split('￥')[1];
	if(val){
		dataInput.val(null);
		$('#selfChoose').text(0)
		$(this).addClass('detaSelect').siblings().removeClass("detaSelect");
		$('#money').html(val)
		console.log(val)
	}
})
//获取输入值
dataInput.focus(function(){
	$('#money').text(0)
	detaLi.removeClass("detaSelect");
	dataInput.keyup(function(){
		inputval = dataInput.val();
		//正则匹配替换非数字字符
		input = inputval.replace(/\D/, '');
		dataInput.val(input);
		$('#selfChoose').text(input*100);
		if(!input || input == 0)
			$('#money').text(0)
		else
			$('#money').text(input)
	})
})
//用户协议
chooseleft.click(function(){
	showChoose.toggleClass('paySure');
	showChoose.toggleClass('paynoSure');
})
//支付请求
$('.payNow').click(function(){
	money = $('#money').text();
	if(money != "0"){
		$.get('/PayAPIView/', {"money": money},function(data){
            console.log(data.code);
            console.log(data.data);
            if(!data.code){
                window.location.href = data.data;
            }
		});
	}else{
		alert('请输入付款金额')
	}
	
})
