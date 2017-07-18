var url = "/UserCenterAPIView/";
var bookUrl = "concret.json";
var bookData = [];
var show = $('#allBook');
var hide = $('#hideBook');
//我的追书
var myBook = new Vue({
	el: "#myBook",
	delimiters: ['[[', ']]'],
	data: {
		myBooks: [],
		bookId: 0
	},
	methods: {								//点击全部追书
		showAll: function(){
			var show = $('#allBook');
			var hide = $('#hideBook');
			show.hide();
			hide.show();
			$.post(bookUrl,
				{"userId": 1},
				function(data){
				myBookChange(data);
				bookData = data;
			})
		show.hide();
		hide.show();
		},
		hideAll: function(){				//点击收回
			var show = $('#allBook');
			var hide = $('#hideBook');
			myBook.myBooks = [bookData.userRunBook[0]];
			hide.hide();
			show.show();
		}
	}
})
//我的钱包
var myMoney = new Vue({

	el: "#myMoney",
	delimiters: ['[[', ']]'],
	data: {
		balance: 0,
		diamondTicket: 0,
		recommendTicket: 0
	}
})
//书评
var bookCommand = new Vue({
	el: "#bookCommand",
	delimiters: ['[[', ']]'],
	data: {
		commands: []
	},
	methods: {
		exitLogin: function(){
            $.get(
                "/UserLogoutAPIView/",
	            {"userId": 1},
                function(data){
                	window.location.href = "/";
                });
		}
	}
})
//我的追书
function myBookChange(data){
/*	userId = data.bookId;*/
	myBook.myBooks = data.userRunBook;
	myBook.bookId = data.bookId;
}
//改变我的钱包
function myMoneyChange(data){
	myMoney.balance = data.balance;
	myMoney.diamondTicket = data.diamondTicket;
	myMoney.recommendTicket = data.recommendTicket;
}
//改变书论函数
function bookCommandChange(data){
	bookCommand.commands = data.bookComment;
}
//页面加载时的请求
$.get(url,
	{"userId": 1},
	function(data){
	    data = $.parseJSON(data);
		myBookChange(data);
		myMoneyChange(data);
		bookCommandChange(data);
	});