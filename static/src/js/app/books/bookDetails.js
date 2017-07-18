var Win = $(window);
 	var bgPeng = $('#bgPeng');
	var pengChang = $('#pengChang');
	var closePen = $('.closePen');
	var root = $('#root');
	var penSubmit = $('#penSubmit');
	var contentSubmit = $('#contentSubmit');
	var fixCommand = $('#fixCommand');
	var raChoose = $('.raChoose');

	var bookId = 0; 		//初始化书籍id
	var val = 0;		//初始化被选中的值
	var penCount = 0;    //初始化输入的数量
	var commentTitle = '' 			//初始化评论标题
	var commentComment = ''			//初始化评论内容
	var penUrl = "/RewardViewAPI/";		//捧场提交的url
	var comUrl = "/CommentViewAPI/";		//评论提交的url
	var url = "/BookInfoViewAPI/";	//页面加载时的url

	//获取bookId
    function getBookId(){
            var url=window.location.href;
            var s=url.split('/');
            var bookId;
            for (x in s){
            var bookIdTest = new RegExp("^[0-9]+$").test(s[x]);
                if (bookIdTest==true){
                    bookId=parseInt(s[x]);
                    return bookId;
                }
            }
        }
	bookId = getBookId();

	//改变信息展示函数
	function showModuleChange(data){
		showModule.title = data.bookInfo.bookName,
		showModule.author = data.bookInfo.author,
		showModule.fontNumber = data.bookInfo.wordNumber,
		showModule.clickNumber = data.bookInfo.clicksNumber,
		showModule.bookFans = data.bookInfo.subscribersNumber,
		showModule.status = data.bookInfo.state,
		showModule.imgSrc = data.bookInfo.coverImg,
		showModule.grounds = data.bookInfo.bookName
	}

	//改变最新更新函数
	function bookRecentlyChange(data){
		bookRecently.timeData = data.bookInfo.updateTime,
		bookRecently.charpterNumber = data.bookInfo.chaptersId,
		bookRecently.charpterTitle = data.bookInfo.chaptersName,
		bookRecently.chaptersType = data.bookInfo.chaptersType
	}

	//改变捧场函数
	function boostChange(data){
		boost.lkNumber = data.bookInfo.reward,
		boost.nm1 = data.bookInfo.catBallNumber,
		boost.nm2 = data.bookInfo.catnipNumber,
		boost.nm3 = data.bookInfo.catStickNumber,
		boost.nm4 = data.bookInfo.catFoodNumber,
		boost.nm5 = data.bookInfo.catFishNumber,
		boost.nm6 = data.bookInfo.catHouseNumber,
		boost.btpersons = data.bookReward
	}

	//改变评论函数
	function bookCommandChange(data){
		bookCommand.commands = data.bookComment;
	}

	//信息展示
	var showModule = new Vue({
			el: "#showModule",
			delimiters: ['[[', ']]'],
			data: {
				title: '',
				author: '',
				fontNumber: 0,
				clickNumber: 0,
				bookFans: 0,
				status: '',
				imgSrc: '',
				grounds: '',
			    bookId: bookId,
			}
		})

	//最新更新
	var bookRecently = new Vue({
			el: "#bookRecently",
			delimiters: ['[[', ']]'],
			data: {
			    bookId: bookId,
				timeData: '',
				charpterNumber: 0,
				charpterTitle: '',
				chaptersType: 0
			}
		})

	//捧场
	var boost = new Vue({
			el: "#boost",
			delimiters: ['[[', ']]'],
			data: {
			    bookId: bookId,
				lkNumber: 0,
				nm1: 0,
				nm2: 0,
				nm3: 0,
				nm4: 0,
				nm5: 0,
				nm6: 0,
				btpersons: []
			},
			//点击捧场时
			methods: {
				showPeng: function(){
					//捧场
					//判断登陆状态，已登陆展示，未登录，跳转登陆界面
					pengChang.show();
				}
			}
		})

	//评论
	var bookCommand = new Vue({
			el: "#bookCommand",
			delimiters: ['[[', ']]'],
			data: {
			    bookId: bookId,
				commands: []
			},
			methods: {
				showCommand: function(){
					//书评
					//判断登陆状态，已登陆展示，未登录，跳转登陆界面
					fixCommand.show();
				}
			}
		})

	//页面加载请求
	$.get("/BookInfoViewAPI/", {"Id": bookId}, function(data){
		data = $.parseJSON(data);
		showModuleChange(data);
		bookRecentlyChange(data);
		boostChange(data);
		bookCommandChange(data);	
	});
	//捧场和评论关闭
	closePen.click(function(){
		pengChang.hide();
		fixCommand.hide();
	})

	//监听窗口滚动事件
	Win.scroll(function(){
	});

	//捧场提交
	penSubmit.click(function(){
		for(var i = 0; i < raChoose.length; i++){
			if(raChoose[i].checked)
				val = raChoose[i].value;
		}
		penCount = $('#penText').val();
		if(penCount > 0 && val)
		{
			$.get(penUrl,
			{

				"rewardType": val,
				"productionNumber": penCount,
				"bookId": bookId
			},
			function(data){
				if(!data.code){
					window.location.href = window.location.href;
					alert("捧场成功");
					pengChang.hide();
				}
				else{
					alert(data.data);
					pengChang.hide();
				}
			})
		}
	})

	//评论提交
	contentSubmit.click(function(){
		commentTitle = $('#addTitle').val();
		commentComment = $('#addText').val();
		if(commentComment && commentComment){
			$.get(comUrl,
			{
				"commentTitle": commentTitle,
				"commentContent": commentComment,
				"bookId": bookId
			},
			function(data){
				if(!data.code){
					bookCommandChange(data);
					$('#addTitle').val('');
					$('#addText').val('');
					fixCommand.hide();
					window.location.href = window.location.href;
				}else{
					alert(data.data)
					fixCommand.hide();
				}
			})
		}
	})

	//输入字数计算
		function countInput(obj) {
			var len = $(obj).val().length;
			if(len < 200) {
				$(".inputSize").html(50 - parseInt(len));
			} else {
				$(".inputSize").html(0);
			}
		}

	//点击追书
    $('#followBook').click(function(){
        $.get("/chaseBooksAPIView/", {"bookId": bookId}, function(data){
        if(!data.code)
            $('#followBook').css('opacity', 0.5).html('已追书')
            })
    })


    //点击自动订阅
    $('#aotoBuy').click(function(){
         $.get("/subscribersAPIView/", {"bookId": bookId}, function(data){
              if(!data.code){
                 $('#aotoBuy').css('opacity', 0.5).html('已订阅')
              }else{
                  alert("余额不足，请充值")
               }
         });
    });

    // 开始阅读

    $(document).ready(function(){
        $('#startRead').attr({href: '/books/' + bookId + '/'+'chapters/'+ 1 +'/'});
    });