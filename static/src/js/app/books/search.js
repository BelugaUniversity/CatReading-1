var v = new Vue({
        delimiters: ['[[', ']]'],
        el: "#chapter",
        data: {
            items: []
        }
    })

    var s = new Vue({
        delimiters: ['[[', ']]'],
        el: "#search",
        data: {
            goal: ""
        }
    })

    var queryKind = 0;

    var url = window.location.search;
    if (url.indexOf("?") != -1) {

        var str = url.substr(1);
        //strs = str.split("=");
        s.goal = decodeURI(str);
        queryKind = 1;
        reqestMore();
    }

    var book = document.getElementById('book');
    var people = document.getElementById('people');
    var query = document.getElementById('queryButton');
    queryKind = 1;

    book.onclick = function() {
        book.checked = people.checked = false;
        book.checked = true;
        queryKind = 1;
    }

    people.onclick = function() {
        people.checked = book.checked = false;
        people.checked = true;
        queryKind = 2;
    }

    queryButton.onclick = function() {
        reqestMore();
    }

    function reqestMore() {
        $.get("/searchBooksViewAPI/", {
            queryString: s.goal,
            queryKind: queryKind
        }, function(data) {
            data = $.parseJSON(data);
            v.items = data.list;
        })
    }



    // function lastPage() {
    //     if (f.pagesNumber > 1) {
    //         f.pagesNumber--;
    //         reqestMore();
    //     }
    // }

    // function nextPage() {
    //     if (f.pagesNumber < v.yeshuNumber) {
    //         f.pagesNumber++;
    //         reqestMore();
    //     }
    // }

    // function jumpPage(value) {
    //     f.pagesNumber = value;
    //     reqestMore();
    // }
