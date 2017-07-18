# **coding: utf-8**`
"""
    Copyright (c), 2016-2017,  beluga Tech.
    File name： view.py
    Description: 阅读应用模块的视图处理
"""


import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, QueryDict
from rest_framework.views import APIView
from .models import BookInfo, BooksContent
from reward.models import Reward
from comment.models import Comment
from .serializers import (
    CompetitiveListSerializers, RankListSerializers,
    ShowImgSerializers, BookInfoSerializers,
    LibrarySerializers, ChaptersSerializers,
    BookHeadInfoSerializers, SearchBooksSerializers
    )
from reward.serializers import BookInfoRewardSerializers
from comment.serializers import BookInfoCommentSerializers
from django.core.paginator import Paginator
from utils import booktype, shortcuts
from datetime import datetime, timedelta
from CatReading.custom_settings import WEBSITE_INFO


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     免费板块的视图渲染应用
"""


class ShowImgViewAPI(APIView):
    def get(self, request):
        books = BookInfo.objects.all()[:3]
        showImgSerializers = ShowImgSerializers(books, many=True)
        showImg = QueryDict(mutable=True)
        showImg['showImg'] = showImgSerializers.data
        return HttpResponse(json.dumps(showImg.dict()))

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     免费板块的视图渲染应用
"""

class FreeCompetitiveViewAPI(APIView):
    def get(self, requset):
        show_img_book = BookInfo.objects.all()[:1].get()
        competitive_list_book = BookInfo.objects.all()[1:6]
        competitive_list_book = CompetitiveListSerializers(competitive_list_book, many=True)
        content = QueryDict(mutable=True)
        content['id'] = show_img_book.id
        content['coverImg'] = show_img_book.coverImg.url
        content['bookName'] = show_img_book.bookName
        content['describe'] = show_img_book.describe
        content['author'] = show_img_book.author
        content['type'] = booktype.bookType[show_img_book.type]
        content['bookList'] = competitive_list_book.data
        free_competitive = QueryDict(mutable=True)
        free_competitive['freeCompetitive'] = content
        return HttpResponse(json.dumps(free_competitive))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     精品板块的视图渲染
"""


class GroundCompetitiveViewAPI(APIView):
    def get(self, request):
        show_img_book = BookInfo.objects.all()[0:1].get()
        competitive_list_book = BookInfo.objects.all()[1:6]
        competitive_list_book = CompetitiveListSerializers(competitive_list_book, many=True)
        content = QueryDict(mutable=True)
        content['id'] = show_img_book.id
        content['coverImg'] = show_img_book.coverImg.url
        content['bookName'] = show_img_book.bookName
        content['describe'] = show_img_book.describe
        content['author'] = show_img_book.author
        content['type'] = booktype.bookType[show_img_book.type]
        content['bookList'] = competitive_list_book.data
        ground_competitive = QueryDict(mutable=True)
        ground_competitive['groundCompetitive'] = content
        return HttpResponse(json.dumps(ground_competitive))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     热书板块的视图渲染
"""


class HotRecommendViewAPI(APIView):
    def get(self, request):
        show_img_book = BookInfo.objects.all()[0:1].get()
        competitive_list_book = BookInfo.objects.all()[1:6]
        competitive_list_book = CompetitiveListSerializers(competitive_list_book, many=True)
        content = QueryDict(mutable=True)
        content['id'] = show_img_book.id
        content['coverImg'] = show_img_book.coverImg.url
        content['bookName'] = show_img_book.bookName
        content['describe'] = show_img_book.describe
        content['author'] = show_img_book.author
        content['type'] =  booktype.bookType[show_img_book.type]
        content['bookList'] = competitive_list_book.data
        free_competitive = QueryDict(mutable=True)
        free_competitive['hotRecommend'] = content
        return HttpResponse(json.dumps(free_competitive))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     新书板块的视图渲染
"""


class NewRecommendViewAPI(APIView):
    def get(self, request):
        showImg = BookInfo.objects.all()[0:4]
        showBook = BookInfo.objects.all()[4:9]
        content = QueryDict(mutable=True)
        showImgSerializers = ShowImgSerializers(showImg, many=True)
        content['imgList'] = showImgSerializers.data
        competitiveListSerializers = CompetitiveListSerializers(showBook, many=True)
        content['bookList'] = competitiveListSerializers.data

        newRecommend = QueryDict(mutable=True)
        newRecommend['newRecommend'] = content
        return HttpResponse(json.dumps(newRecommend.dict()))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     排行榜的视图渲染，
"""


class RankListViewAPI(APIView):
    def get(self, request):
        book = BookInfo.objects.all()[0:10]
        rankListSerializers = RankListSerializers(book, many=True)
        rank = QueryDict(mutable=True)
        rank['listClick'] = rankListSerializers.data
        rank['listRun'] = rankListSerializers.data
        rank['listPay'] = rankListSerializers.data
        return HttpResponse(json.dumps(rank.dict()))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     详情页头部渲染
"""


class BookInfoHeadViewAPI(APIView):
    def get(self, request):
        bookId = request.GET['bookId']
        book = BookInfo.objects.filter(id=bookId).get()
        bookHeadInfoSerializers = BookHeadInfoSerializers(book)
        bookHeadInfo = QueryDict(mutable=True)
        bookHeadInfo['bookHeadInfo'] = bookHeadInfoSerializers.data
        bookHeadInfo['chaptersNumber'] = book.chaptersNumber

        return HttpResponse(json.dumps(bookHeadInfo.dict()))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     详情页
"""


class BookInfoViewAPI(APIView):
    def get(self, request):
        bookId = request.GET.get("Id")
        book = BookInfo.objects.get(id=bookId)
        serializers = BookInfoSerializers(book)
        bookInfo = QueryDict(mutable=True)
        bookInfo['bookInfo'] = serializers.data
        comments = Comment.objects.filter(bookId=bookId).all()[0:3]
        bookInfoCommentSerializers = BookInfoCommentSerializers(comments, many=True)
        bookInfo['bookComment'] = bookInfoCommentSerializers.data
        rewards = Reward.objects.filter(bookId=bookId).all()[0:3]
        bookInfoRewardSerializers = BookInfoRewardSerializers(rewards, many=True)
        bookInfo['bookReward'] = bookInfoRewardSerializers.data
        return HttpResponse(json.dumps(bookInfo.dict()))


"""
    Author:	         毛毛
    Version:         0.02v
    Date:            2017/03/30
    Description:     详情页尾部渲染
    request:
        字段名称     bookId     pagesNumber     isOrder
        描述        书籍Id      请求条数         顺序
    response:
        字段名称       chaptersNumber      chapterId      chaptersName
        描述    　     章节总数             章节数          章节名
"""


class ChaptersViewAPI(APIView):

    def get(self, request):
        numPage = request.GET['numPage']
        bookId = request.GET['bookId']
        isOrder = request.GET['isOrder']

        chapters = ""

        if "true" == isOrder:
            chapters = BooksContent.objects.filter(BookInfo__id=bookId).all()
        elif "false == isOrder":
            chapters = BooksContent.objects.filter(BookInfo__id=bookId).order_by('-chaptersId').all()
        book = BookInfo.objects.get(id=bookId)
        # chapters = BooksContent.objects.filter(BookInfo__id=bookId).all()
        paginator = Paginator(chapters, 5)
        serializers = ChaptersSerializers(paginator.page(numPage).object_list, many=True)
        content = QueryDict(mutable=True)
        content['bookName'] = book.bookName
        content['chaptersList'] = serializers.data
        content['pageNumber'] = paginator.num_pages
        return HttpResponse(json.dumps(content.dict()))


    """

        Author:             毛毛

        Version:         0.01v

        Date:            2017/05/29

        Description:     书库

        request: type, wordNumbers, bookHot, updateTime, state, bookMoney, pagesNumber

    """



class LibraryAPIView(APIView):

    def get(self, request):

        Type = int(request.GET['type'])
        wordNumbers = int(request.GET['wordNumber'])
        updateTime = int(request.GET['updateTime'])
        state = int(request.GET['state'])
        bookMoney = int(request.GET['bookMoney'])
        pagesNumber = request.GET['pagesNumber']
        clicksNumber = request.GET['bookHot']
        books = BookInfo.objects.all()
        endTime = datetime.now()

        if Type is not 0:
            books = books.filter(type=Type)

        # if wordNumbers is not 0:
        #     if wordNumbers is 1:
        #         books = books.filter(wordNumber__lt=300000)
        #
        #     elif wordNumbers is 2:
        #         books = books.filter(wordNumber__range=(300000, 500000))
        #
        #     elif wordNumbers is 3:
        #         books = books.filter(wordNumber__range=(500000, 1000000))
        #     else:
        #         books = books.filter(wordNumber__gt=1000000)
        #
        # if updateTime is not 0:
        #     if updateTime is 1:
        #         startTime = (endTime - timedelta(days=3))
        #         books = books.filter(updateTime__range=(startTime, endTime))
        #     elif updateTime is 2:
        #         startTime = (endTime - timedelta(days=7))
        #         books = books.filter(updateTime__range=(startTime, endTime))
        #     else:
        #         startTime = (endTime - timedelta(days=30))
        #         books = books.filter(updateTime__range=(startTime, endTime))
        #
        # if state is not 0:
        #     books = books.filter(state=state-1)
        # if bookMoney is not 0:
        #     books = books.filter(bookMoney=bookMoney-1)

        paginator = Paginator(books, 10)
        serializers = LibrarySerializers(paginator.page(pagesNumber).object_list, many=True)
        library = QueryDict(mutable=True)
        library['list'] = serializers.data
        library['yeshuNumber'] = books.count()
        return HttpResponse(json.dumps(library.dict()))





"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     免费榜的视图渲染应用
"""


def ReadingViewAPI(request):

    if request.method == 'GET':
        bookId = request.GET['bookId']
        chaptersId = request.GET['chaptersId']
        book = BookInfo.objects.get(id=bookId)
        bookChapter = BooksContent.objects.filter(BookInfo__id=bookId).filter(chaptersId=chaptersId).get()
        response = JsonResponse({'bookName': book.bookName, 'chaptersNumber': book.chaptersNumber, 'chaptersName': bookChapter.chaptersName,
                                 'chaptersContent': bookChapter.chaptersContent})
        return HttpResponse(response)
    else:
        return Http404

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/07/07
    Description:     搜书页面APIView
"""


class searchBooksViewAPI(APIView):
    def get(self, request):
        temp = request.GET['queryString']
        method = int(request.GET['queryKind'])
        if method < 1:
            books = BookInfo.objects.aggregate(Q(bookName__contains=temp) | Q(author__contains=temp))
        elif method == 1:
          books = BookInfo.objects.filter(bookName__contains=temp)
        else:
            books = BookInfo.objects.filter(author__contains=temp)
        searchcontent = SearchBooksSerializers(books, many=True)
        result = QueryDict(mutable=True)
        result['list'] = searchcontent.data
        return HttpResponse(json.dumps(result.dict()))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/07/08
    Description:     加入追书
"""


class chaseBooksAPIView(APIView):

    def get(self, request):
        return shortcuts.success_response("请先登陆")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/07/08
    Description:     自动订阅
"""


class subscribersAPIView(APIView):

    def get(self, request):
        return shortcuts.success_response("请登陆登陆")


"""
    Author:	         cc
    Version:         0.01v
    Date:            2017/03/30
    Description:     首页页面
"""


def indexPage(request):
    return render(request, "reading/index.html", WEBSITE_INFO)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     阅读页面
"""


def rankPage(request):
    return render(request, "reading/books/rank.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书库页面
"""


def libraryPage(request):
    return render(request, "reading/books/library.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     阅读页面
"""


def readingPage(request):
    return render(request, "reading/books/reading.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     阅读页面
"""


def bookDetailsPage(request):
    return render(request, "reading/books/bookDetails.html")


"""
    Author:	         马承成
    Version:         0.01v
    Date:            2017/03/30
    Description:     章节目录页面
"""

def cataloguePage(request):
    return render(request, "reading/books/catalogue.html")

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书籍评论页面
"""


def bookCommentPage(request):
    return render(request, "reading/books/comment.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书籍打赏页面

"""
def bookRewardPage(request):
    return render(request, "reading/books/reward.html")

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书籍搜索页面

"""
def searchPage(request):
    return render(request, "reading/books/search.html")
