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
from rest_framework.views import APIView, Response
from .models import BookInfo, BooksContent, BooksChase, BooksSubscribe
from reward.models import Reward
from comment.models import Comment
from account.models import User
from .serializers import (
    CompetitiveListSerializers, RankListSerializers,
    ShowImgSerializers, BookInfoSerializers,
    LibrarySerializers, ChaptersSerializers,
    BookHeadInfoSerializers, SearchBooksSerializers
    )
from reward.serializers import BookInfoRewardSerializers
from comment.serializers import BookInfoCommentSerializers
from django.core.paginator import Paginator
from django.db.models import Q
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

# """
#     Author:	         毛毛
#     Version:         0.01v
#     Date:            2017/09/12
#     Description:     增减追书测试
# """
#
#
# class BookChaseViewAPI(APIView):
#     def get(self, request):
#         book = BookInfo.objects.get(id=4)
#         wordNumber = book.wordNumber
#         author = book.author
#         chaptersNumber = book.chaptersNumber
#         bookName = book.bookName
#         coverImg = book.coverImg
#         bookstate = book.state
#         testimonials = book.testimonials
#         content = BooksContent.objects.filter(chaptersId=book.chaptersNumber).get()
#         chaptersName = content.chaptersName
#         bookChase = BooksChase(bookId=4, userId=1, wordNumber=wordNumber, bookName=bookName,
#                                chaptersNumber=chaptersNumber, author=author,
#                                chaptersName=chaptersName, coverImg=coverImg,
#                                state=bookstate, testimonials=testimonials)
#         bookChase.save()
#         book.chaseBooksNumber += 1
#         book.save()
#         return shortcuts.success_response(data="追书成功")


class BookChaseViewAPI(APIView):
    @csrf_exempt
    def POST(self, request):
        bookid = request.POST.get("bookId")
        state = request.POST.get("isFollowed")
        userid = User.request.userId
        if state is 0:
            book = BooksChase.object.filter(Q(bookId=bookid) & Q(userId=userid))
            book.delete()
            book.chaseBooksNumber -= 1
            book.save()
            return shortcuts.success_response(data="取消追书")
        else:
            book = BookInfo.objects.filter(id=bookid).get()
            wordNumber = book.wordNumber
            author = book.author
            chaptersNumber = book.chaptersNumber
            bookName = book.bookName
            coverImg = book.coverImg
            bookstate = book.state
            testimonals = book.testimonals
            content = BooksContent.objects.filter(chaptersId=chaptersNumber).get()
            chaptersName = content.chaptersName
            bookchase = BooksChase(bookId=bookid, userId=userid, wordNumber=wordNumber, bookName=bookName,
                                   author=author, chaptersNumber=chaptersNumber, chaptersName=chaptersName,
                                   coverImg=coverImg, state=bookstate, testimonals=testimonals)
            bookchase.save()
            book.chaseBooksNumber += 1
            book.save()
            return shortcuts.success_response(data="追书成功")


# """
#     Author:	         毛毛
#     Version:         0.01v
#     Date:            2017/09/15
#     Description:     记录用户追书
# """
# class recordBooksChaseViewAPI(APIView):
#     def POST(self, request):
#         userid = request.POST.get("userId")
#         bookid = request.POST.get("bookId")
#         chaptersnumber = request.POST.get("chaptersNumber")
#         books = BooksChase.object.filter(Q(bookId=bookid) & Q(userId=userid)).get()
#         books.chaptersName = BooksContent.object.filter(chaptersId=chaptersnumber).get().chaptersName
#         books.chaptersNumber = chaptersnumber
#         books.save()
#         return HttpResponse(state=200)



"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/09/16
    Description:     增减订阅测试
"""


class BookChaseViewAPI(APIView):
    def get(self, request):
        book = BookInfo.objects.get(id=4)
        wordNumber = book.wordNumber
        author = book.author
        chaptersNumber = book.chaptersNumber
        bookName = book.bookName
        coverImg = book.coverImg
        bookstate = book.state
        testimonials = book.testimonials
        content = BooksContent.objects.filter(chaptersId=book.chaptersNumber).get()
        chaptersName = content.chaptersName
        bookChase = BooksSubscribe(bookId=4, userId=1, wordNumber=wordNumber, bookName=bookName,
                                   chaptersNumber=chaptersNumber, author=author,
                                   chaptersName=chaptersName, coverImg=coverImg,
                                   state=bookstate, testimonials=testimonials)
        bookChase.save()
        book.subscribersNumber += 1
        book.save()
        return shortcuts.success_response(data="订阅成功")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/09/16
    Description:     增减订阅
"""


class SubscribeBooksViewAPI(APIView):
    @csrf_exempt
    def POST(self, request):
        bookid = request.POST.get("bookId")
        state = request.POST.get("isSubscribed")
        userid = User.request.userId
        if state is 0:
            book = BooksSubscribe.object.filter(Q(bookId=bookid) & Q(userId=userid))
            book.delete()
            book.subscribersNumber -= 1
            book.save()
            return shortcuts.success_response(data="取消订阅")
        else:
            book = BookInfo.objects.filter(id=bookid).get()
            wordNumber = book.wordNumber
            author = book.author
            chaptersNumber = book.chaptersNumber
            bookName = book.bookName
            coverImg = book.coverImg
            bookstate = book.state
            testimonals = book.testimonals
            content = BooksContent.objects.filter(chaptersId=chaptersNumber).get()
            chaptersName = content.chaptersName
            bookchase = BooksSubscribe(bookId=bookid, userId=userid, wordNumber=wordNumber, bookName=bookName,
                                       author=author, chaptersNumber=chaptersNumber, chaptersName=chaptersName,
                                       coverImg=coverImg, state=bookstate, testimonals=testimonals)
            bookchase.save()
            book.subscribersNumber += 1
            book.save()
            return shortcuts.success_response(data="订阅成功")



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
        updatetime = int(request.GET['updateTime'])
        state = int(request.GET['state'])
        bookMoney = int(request.GET['bookMoney'])
        pagesNumber = int(request.GET['pagesNumber'])
        bookHot = int(request.GET['bookHot'])
        books = BookInfo.objects.all()
        endTime = datetime.now()

        if Type is not 0:
            books = books.filter(type=Type)

        if wordNumbers is not 0:
            if wordNumbers is 1:
                books = books.filter(wordNumber__lte=30)

            elif wordNumbers is 2:
                books = books.filter(wordNumber__range=(30, 50))

            elif wordNumbers is 3:
                books = books.filter(wordNumber__range=(50, 100))
            else:
                books = books.filter(wordNumber__gte=100)

        if bookHot is not 0:
            if bookHot is 1:
                books = books.filter(hotBook=1)
            elif bookHot is 2:
                books = books.filter(hotBook=2)
            elif bookHot is 3:
                books = books.filter(hotBook=3)
            elif bookHot is 4:
                books = books.filter(hotBook=4)
            else:
                books = books.filter(hotBook=5)

        if updatetime is not 0:
            if updatetime is 1:
                startTime = (endTime - timedelta(days=3))
                books = books.filter(updateTime__range=(startTime, endTime))
            elif updatetime is 2:
                startTime = (endTime - timedelta(days=7))
                books = books.filter(updateTime__range=(startTime, endTime))
            else:
                startTime = (endTime - timedelta(days=30))
                books = books.filter(updateTime__range=(startTime, endTime))

        if state is not 0:
            books = books.filter(state=state-1)

        if bookMoney is not 0:
            books = books.filter(BookInfo__bookMoney=bookMoney-1)

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
