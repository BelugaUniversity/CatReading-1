var bookType = new Array ()
bookType[0] = "不限"
bookType[1] = "仙剑"
bookType[2] = "玄幻"
bookType[3] = "悬疑"
bookType[4] = "奇幻"
bookType[5] = "军事"
bookType[6] = "历史"
bookType[7] = "竞技"
bookType[8] = "科幻"
bookType[9] = "军事"
bookType[10] = "校园"
bookType[11] = "社会"
bookType[12] = "其它"
/*var rankClick = $('#rankClick');
var rankPay = $('#rankPay');
var rankRun = $('#rankRun');
var listClick = $('#listClick');
var listPay = $('#listPay');
var listRun = $('#listRun');
rankClick.click(function(){
	if(listClick.css('display') == "none"){
		listClick.show().siblings().hide();
		rankClick.addClass("active").siblings().removeClass("active");
	}
})
rankPay.click(function(){
	if(listPay.css('display') == "none"){
		listPay.show().siblings().hide();
		rankPay.addClass("active").siblings().removeClass("active");
	}
})
rankRun.click(function(){
	if(listRun.css('display') == "none"){
		listRun.show().siblings().hide();
		rankRun.addClass("active").siblings().removeClass("active");
	}
})*/
var search = $("#searchText");
var go = $("#searchButton");
go.click(function(){	
	window.location.href = "/search" + "?" + search.val();
})


	

var urlShowImg = "/ShowImgViewAPI/";
var urlhotRecommend = "/HotRecommendViewAPI/";
var urlfreeCompetitive = "/FreeCompetitiveViewAPI/";
var urlgroundCompetitive = "/GroundCompetitiveViewAPI/";
var urlNewRecommend = "/NewRecommendViewAPI/";
var urlRank = "/RankListViewAPI/";
$.get(urlShowImg, {"firstPage": "true"}, function(data){
		data = $.parseJSON(data);
		//数据绑定
		var showImg = new Vue({			//展示图片区
			delimiters: ['[[', ']]'],
			el: "#showImg",
			data: {
				contents: data.showImg
			}
		})
})

$.get(urlhotRecommend, {"firstPage": "true"}, function(data){
		//数据绑定
		data = $.parseJSON(data);
		<!--console.log(data.ty);-->
		var hotRecommend = new Vue({			//热门推荐区
			delimiters: ['[[', ']]'],
			el: "#hotModule",
			data: {
				hots: data.hotRecommend
			}
		})
})

$.get(urlfreeCompetitive, {"firstPage": "true"}, function(data){
		//数据绑定
	    data = $.parseJSON(data);
		var freeCompetitive = new Vue({			//免费精品区
			delimiters: ['[[', ']]'],
			el: "#freeModule",
			data: {
				frees: data.freeCompetitive
			}
		})
})

$.get(urlgroundCompetitive, {"firstPage": "true"}, function(data){
		//数据绑定
		data = $.parseJSON(data);
		var groundCompetitive = new Vue({			//上架精品区
			delimiters: ['[[', ']]'],
			el: "#groundModule",
			data: {
				grounds: data.groundCompetitive
			}
		})
})

$.get(urlNewRecommend, {"firstPage": "true"}, function(data){
		//数据绑定
	    data = $.parseJSON(data);
		var newRecommend = new Vue({			//新书推荐区
			delimiters: ['[[', ']]'],
			el: "#newModule",
			data: {
				news: data.newRecommend
			}
		})
})

$.get(urlRank, {"firstPage": "true"}, function(data){
	    data = $.parseJSON(data);
		//数据绑定
		var rank = new Vue({			//榜单区
			delimiters: ['[[', ']]'],
			el: "#rank",
			data: {
				clicks: data.listClick,
				pays: data.listPay,
				runs: data.listRun
			},
			methods: {
				rankClick: function(){
					var rankClick = $('#rankClick');
					var listClick = $('#listClick');
					if(listClick.css('display') == "none"){
						listClick.show().siblings().hide();
						rankClick.addClass("active").siblings().removeClass("active");
					}
				},
				rankPay: function(){
					var rankPay = $('#rankPay');
					var listPay = $('#listPay');
					if(listPay.css('display') == "none"){
						listPay.show().siblings().hide();
						rankPay.addClass("active").siblings().removeClass("active");
					}
				},
				rankRun: function(){
					var rankRun = $('#rankRun');
					var listRun = $('#listRun');
					if(listRun.css('display') == "none"){
						listRun.show().siblings().hide();
						rankRun.addClass("active").siblings().removeClass("active");
					}
				}
			}
		})
})