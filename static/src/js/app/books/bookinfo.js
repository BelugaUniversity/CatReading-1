var v = new Vue({
	delimiters: ['[[', ']]'],
	el:"#app",
	data:{
		pages:10,
		now:1
	},
	methods:{

		//TODO

		//上一页
		prePage:function(){
			if (this.now >1 && this.now<=this.pages) this.now-=1;
			$.get("/ChaptersViewAPI/", {pagesNumber: this.now, id: b.id, isZheng: c.active2},function(data){
				data = $.parseJSON(data);
				console.log(data);
				console.log(this.now);
				if (c.active2){
					t.titles=data.chaptersList;
				}
				else{
					t.ntitles=data.chaptersList;
				}
			})
		},

		//下一页
		nextPage:function(){
			if (this.now >=1 && this.now<this.pages) this.now=parseInt(this.now)+1;
			$.get("/ChaptersViewAPI/", {pagesNumber: this.now, id: b.id, isZheng: c.active2},function(data){
				data = $.parseJSON(data);
				console.log(data);
				console.log(this.now);
				if (c.active2){
					t.titles=data.chaptersList;
				}
				else{
					t.ntitles=data.chaptersList;
				}
			})
		}
	}
})
var t = new Vue({
	delimiters: ['[[', ']]'],
	el:"#all",
	data:{
		zheng:false,
		ni:true,
		bookId:0,
		titles:[

		],
		ntitles:[

		]
	}
})
var c = new Vue({
	delimiters: ['[[', ']]'],
	el:"#click",
	data:{
		active1:true,
		active2:false
	},
	methods:{
		click1:function(){
			if (this.active1==true) {return ;}
			this.active1=true;
			this.active2=false;
			t.zheng=false;
			t.ni=true;

			//TODO

			$.get("/ChaptersViewAPI/", {pagesNumber: v.now, id: b.id, isZheng: this.active2} ,function(data){
				data = $.parseJSON(data);
				console.log(v.now);
              			t.ntitles=data.chaptersList;
			})
		},
		click2:function(){
			if (this.active2==true) {return ;}
			this.active1=false;
			this.active2=true;
			t.zheng=true;
			t.ni=false;

			//TODO

			$.get("/ChaptersViewAPI/", {pagesNumber: now, id: b.id, isZheng: this.active2}, function(data){
				data = $.parseJSON(data);
				console.log(v.now);
				t.titles=data.chaptersList;
			})
		}
	}
})

var b = new Vue({
	delimiters: ['[[', ']]'],
	el:"#booknow",
	data:{
			id:1,
			coverurl: "",
			title: "",
			wordNumber: 0,
			author: "",
			clicksNumber: 0,
			chaseBooksNumber: 0,
			state: 1
	},
	methods:{
		clone:function(a){
			this.id=a.bookId;
			this.coverurl=a.coverImg;
			this.title=a.name;
			this.wordNumber=a.wordNumber;
			this.author=a.author;
			this.clicksNumber=a.clicksNumber;
			this.chaseBooksNumber=a.chaseBooksNumber;
			this.state=a.state;
		}
	}
})


//TODO
function turn(pagenow){
	v.now=pagenow;
	$.get("/ChaptersViewAPI/", {pagesNumber: v.now, id: b.id, isZheng: c.active2},function(data){
		data = $.parseJSON(data);
		console.log(data);
		console.log(v.now);
		if (c.active2){
			t.titles=data.chaptersList;
		}
		else{
			t.ntitles=data.chaptersList;
		}
	})
}

// 正则解析url携带参数
$(document).ready(function(){
    var url=window.location.href;
    var s = url.split('/')
    var bookId;
    for(x in s){
        var bookIdTest = new RegExp("^[0-9]+$").test(s[x])
        if(bookIdTest==true){
            bookId = parseInt(s[x]);
            $.get("/BookInfoHeadViewAPI/", {"bookId": bookId}, function(data){
                data = $.parseJSON(data);
                console.log(data);
                b.clone(data.bookHeadInfo);
                t.bookId=b.id;
                v.pages=data.chaptersNumber;
            })

            $.get("/ChaptersViewAPI/",  {"pagesNumber": 1, "bookId": bookId, isZheng: false}, function(data){
            console.log(bookId);
            data = $.parseJSON(data);
            console.log(data.chaptersList);
            t.ntitles=data.chaptersList;
})
            return true;
        }
    }
});

