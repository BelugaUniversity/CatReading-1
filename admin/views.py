# **coding: utf-8**
"""
    Copyright (c), 2016-2017,  beluga Tech.
    File name： view.py
    Description: 管理员应用模块的视图处理

"""

import os
from utils import shortcuts
from django.conf import settings
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .serializers import BookListSerializers, CreateChapterSerializers, ChaptersListSerializers, ShowBookInfoSerializers, EditBookInfoSerializers, EditChapterListSerializers, ShowChapterSerializers, ShowUserListSerializers
from books.models import BookInfo, BooksContent
from account.models import User
from django.core.paginator import Paginator
from django.http import QueryDict, HttpResponse, JsonResponse, HttpResponseRedirect
import json


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书籍列表接口
    request:
        字段名称     pagesNumber
        描述        页数
    response:
        字段名称    bookNumber    bookId      coverImg　  subscribersNumber   bookName  chaptersNumber    chaptersName    bookType       state
        描述       总书籍数　    书籍id       封面          追书量              书名       最新章节数          最新章节        书籍类型        书籍状态
"""


class BookListAPIView(APIView):

    def get(self, request):
        pagesNumber = request.GET['numPage']
        book = BookInfo.objects.all()
        paginator = Paginator(book, 10)
        serializers = BookListSerializers(paginator.page(pagesNumber).object_list, many=True)
        content = QueryDict(mutable=True)
        content['bookList'] = serializers.data
        content['pageNumber'] = paginator.num_pages
        content['bookNumber'] = paginator.count
        return HttpResponse(json.dumps(content.dict()))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书籍创建接口
    request:
        字段名称     bookName   author      type        describe
        描述        书名        作者      　类型         作品介绍
"""


class CreateBookAPIView(APIView):

    @ csrf_exempt
    def post(self, request):
        bookName = request.POST.get("bookName")
        author = request.POST.get("author")
        type = request.POST.get("type")
        describe = request.POST.get("describe")
        book = BookInfo(bookName=bookName, author=author, type=type, describe=describe)
        book.save()
        message = "书籍创建成功"
        return shortcuts.success_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书籍删除接口
    request:
        字段名称    bookId
        描述        书籍id
"""


class DeleteBookAPIView(APIView):

    def get(self, request):
        bookId = request.GET.get("bookId")
        book = BookInfo.objects.get(id=bookId)
        book.delete()
        message = "书籍删除成功"
        return shortcuts.success_response(message)



"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书籍信息修改页显示接口
    request:
        字段名称    bookId
        描述        书籍id
    request:
        字段名称     bookName   author      chaseBooksNumber      wordNumber      state       type        describe
        描述        书名        作者      　 追书数                字数             状态        类型         作品介绍
"""


class ShowBookInfoAPIView(APIView):

    def get(self, request):
        bookId = request.GET.get("bookId")
        book = BookInfo.objects.get(id=bookId)
        serializer = ShowBookInfoSerializers(book)
        return HttpResponse(json.dumps(serializer.data))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书籍信息修改接口
    request:
        字段名称    bookId
        描述        书籍id
    request:
        字段名称     bookId     bookName   author      state       type        describe
        描述        书籍id      书名        作者        状态        类型         作品介绍
"""


class EditBookInfoAPIView(APIView):

    @ csrf_exempt
    def post(self, request):
        serializer = EditBookInfoSerializers(request.data)
        data = serializer.data
        book = BookInfo.objects.get(id=data['id'])
        book.name = data['bookName']
        book.author = data['author']
        book.state = data['state']
        book.type = data['type']
        book.describe = data['describe']
        if "" == data['testimonials']:
            book.testimonials = data['testimonials']
        else:
            book.testimonials = data['testimonials'] + " : "
        book.save()
        message = "书籍修改成功"
        return shortcuts.success_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
	Description:     删除章节接口
   	request:
        	字段名称     bookId　　      chapterId	chaptersName    　chaptersType    chaptersContent	chaptersState
        	描述        书籍id          章节id	     章节名            章节类型        章节内容		    章节发布状态
	respone:
        	字段名称    code      　　　data
         	描述        请求状态     传递消息
"""


class CreateChapterAPIView(APIView):

    @ csrf_exempt
    def post(self, request):
        serializer = CreateChapterSerializers(request.data)
        data = serializer.data
        book = BookInfo.objects.get(id=data['bookId'])
        chaptersId = book.chaptersNumber+1
        book.add_chapters_number()
        bookContent = BooksContent(BookInfo=book, chaptersId=chaptersId, chaptersName=data['chaptersName'], chaptersType=data['chaptersType'], chaptersContent=data['chaptersContent'], chaptersState=data['chaptersState'])
        bookContent.wordNumber = len(data['chaptersContent'])
        bookContent.save()
        print u"章节内容" + data['chaptersContent']
        message = "章节创建成功"
        return shortcuts.success_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书籍发布接口
    request:
        字段名称    chaptersId      chaptersName    　chaptersType    　chaptersContent
        描述        章节数           章节名            章节类型    　     章节内容
"""


class ReleaseChapterAPIView(APIView):

    @ csrf_exempt
    def post(self, request):
        serializer = CreateChapterSerializers(request.data)
        data = serializer.data
        book = BookInfo.objects.get(id=data['bookId'])
        chaptersId = book.chaptersNumber+1
        book.add_chapters_number()
        try:
            chapter = BooksContent.objects.get(bookInfo=book, chaptersName=data['chaptersName'], chaptersContent=data['chaptersContent'])
            chapter.chaptersType = data['chaptersType']
            chapter.chaptersState = data['chaptersState']
            chapter.save()
        except BooksContent.DoesNotExist:
            bookContent = BooksContent(BookInfo=book, chaptersId=chaptersId, chaptersName=data['chaptersName'], chaptersType=data['chaptersType'], chaptersContent=data['chaptersContent'], chaptersState=data['chaptersState'])
            bookContent.wordNumber = len(data['chaptersContent'])
            bookContent.save()
        # print data['chaptersContent']
        message = "章节创建成功"
        return shortcuts.success_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     已发布章节书籍章节列表接口
    request:
        字段名称     bookId         pagesNumber
        描述        书籍id          页数
    response:
        字段名称    chaptersId      chaptersName    chaptersType    updateTime      　chaptersPV   chaptersType      wordNumber
        描述        章节数           章节名          章节类型         更新时间          浏览量         章节类型          章节字数
"""


class ChaptersListAPIView(APIView):

    def get(self, request):
        bookId = request.GET.get("bookId")
        pagesNumber = request.GET.get("pagesNumber")
        book = BookInfo.objects.get(id=bookId)
        chapters = BooksContent.objects.filter(BookInfo__id=bookId).all()
        paginator = Paginator(chapters, 10)
        serializers = ChaptersListSerializers(paginator.page(pagesNumber).object_list, many=True)
        content = QueryDict(mutable=True)
        content['name'] = book.bookName
        content['chaptersList'] = serializers.data
        content['pageNumber'] = paginator.num_pages
        content['chaptersNumber'] = paginator.count
        print paginator.count
        return HttpResponse(json.dumps(content.dict()))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     草稿箱书籍章节列表接口
    request:
        字段名称     bookId
        描述        书籍id
    response:
        字段名称    chaptersNumber       chaptersId      chaptersName    　wordNumber    　   updateTime
        描述        未发布章节总数         章节数           章节名            字数    　         更新时间
"""


class EditChapterListAPIView(APIView):

    def get(self, request):
        bookId = request.GET.get("bookId")
        book = BookInfo.objects.get(id=bookId)
        chapters = BooksContent.objects.filter(BookInfo__id=bookId).all()
        serializers = EditChapterListSerializers(chapters, many=True)
        content = QueryDict(mutable=True)
        content['chaptersList'] = serializers.data
        content['chaptersNumber'] = 1
        content['name'] = book.bookName
        content['chaptersNumber'] = book.chaptersNumber
        message = "章节内容显示成功"
        return HttpResponse(json.dumps(content.dict()))


class RecommendBookAPIView(APIView):

    def get(self, request):
        bookId = request.GET.get("bookId")
        testimonials = request.GET.get("testimonials")
        hotBook = request.GET.get("hotBook")
        freeBook = request.GET.get("freeBook")
        rankBook = request.GET.get("rankBook")
        newBook = request.GET.get("newBook")
        headImgBook = request.GET.get("headImgBook")

        book = BookInfo.objects.get(id=bookId)
        book.testimonials = testimonials
        book.hotBook = hotBook
        book.freeBook = freeBook
        book.rankBook = rankBook
        book.newBook = newBook
        book.headImgBook = headImgBook
        book.save()
        message = u"推荐成功"
        return shortcuts.success_response(message)

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书籍章节内容修改接口
    request:
        字段名称    chaptersId      chaptersName    　chaptersType    　chaptersContent
        描述        章节数           章节名            章节类型    　     章节内容
"""


class EditChapterAPIView(APIView):

    @ csrf_exempt
    def post(self, request):
        message = "章节内容修改成功"
        return shortcuts.success_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     书籍章节内容修改显示接口
    request:
        字段名称     bookId　　      chapterId
        描述        书籍id          章节id
    response:
        字段名称    chaptersId      chaptersName    　chaptersType    　chaptersContent
        描述        章节数           章节名            章节类型    　     章节内容
"""


class ShowChapterAPIView(APIView):

    def get(self, request):
        bookId =request.GET.get("bookId")
        chaptersId =request.GET.get("chaptersId")
        chapter = BooksContent.objects.filter(BookInfo__id=bookId).filter(chaptersId=chaptersId).get()
        serializer = ShowChapterSerializers(chapter)
        return HttpResponse(json.dumps(serializer.data))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     章节删除接口
        request:
        	字段名称    bookId      chapterId
         	描述        书籍id      章节id
	respone:
        	字段名称    code      　　　data
         	描述        请求状态     传递消息
"""


class DeleteChapterAPIView(APIView):

    def get(self, request):
        id = request.GET.get("bookId")
        chapterId = request.GET.get("chaptersId")
        book = BookInfo.objects.get(id=id)
        print chapterId
        chapter = BooksContent.objects.filter(BookInfo__id=id).filter(chaptersId=chapterId).get()
        chapter.delete()
        book.subtract_chapters_number()
        message = "章节删除成功"
        return shortcuts.success_response(message)


class WordCountAPIView(APIView):

    def get(self, request):
        id = request.GET.get("bookId")
        chaptersId = request.GET.get("chaptersId")
        chapter = BooksContent.objects.filter(BookInfo__id=id).filter(chaptersId=chaptersId).get()
        response = JsonResponse({'wordNumber': chapter.wordNumber})
        return HttpResponse(response)



class CoverImgUploadAPIView(APIView):
    def post(self, request):
        if "file" not in request.FILES:
            return error_response(u"文件上传失败")

        f = request.FILES["file"]
        if f.size > 1024 * 1024:
            return error_response(u"图片过大")
        if os.path.splitext(f.name)[-1].lower() not in [".gif", ".jpg", ".jpeg", ".bmp", ".png"]:
            return error_response(u"需要上传图片格式")
        name = "CoverImg_" + shortcuts.rand_str(5) + os.path.splitext(f.name)[-1]
        with open(os.path.join(settings.IMAGE_UPLOAD_DIR, name), "wb") as img:
            for chunk in request.FILES["file"]:
                img.write(chunk)
        # print os.path.join(settings.IMAGE_UPLOAD_DIR, name)
        bookId = request.POST.get("bookId")
        book = BookInfo.objects.get(id=bookId)
        book.coverImg = name;
        book.save()
        return shortcuts.success_response(name)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     用户管理显示接口
    response:
        字段名称    chaptersId      chaptersName    　chaptersType    　chaptersContent
        描述        章节数           章节名            章节类型    　     章节内容
"""


class ShowUserListAPIView(APIView):
    def get(self, request):
        numPage = request.GET.get("numPage")
        users = User.objects.all()
        paginator = Paginator(users, 5)
        pageNumber = paginator.num_pages
        # serializers = ShowUserListSerializers(paginator.page(numPage).object_list, many=True)
        serializers = ShowUserListSerializers(users, many=True)
        content = QueryDict(mutable=True)
        content['userInfo'] = serializers.data
        if pageNumber >= 5:
            pageNumber = 5
        content['pageNumber'] = pageNumber
        return HttpResponse(json.dumps(content.dict()))


class EditUserAPIView(APIView):

    def post(self, request):
        userId = request.POST.get("userId")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userPassword = request.POST.get("userPassword")
        userType = request.POST.get("userType")
        user = User.objects.get(id=userId)
        print userPassword
        if userPassword is not None:
            user.set_password(userPassword)
        user.userName = userName
        user.phone = userPhone
        user.save()
        message = "用户信息修改成功"
        return shortcuts.success_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     管理员登录页面
"""


def AdminLoginkPage(request):
    return render(request, "admin/login.html")

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     创建书籍页面
"""


def createBookPage(request):
    return render(request, "admin/createbook.html")

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     创建书籍页面
"""


def BookManagerPage(request):
    return render(request, "admin/bookmanager.html")

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     创建书籍页面
"""


def UserManagerPage(request):
    return render(request, "admin/user.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     创建书籍页面
"""


def dataStatisticsPage(request):
    return render(request, "admin/datastatistics.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     创建书籍页面
"""


def WriteChaptersPage(request):
    return render(request, "admin/write.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     创建书籍页面
"""


def PublishPage(request):
    return render(request, "admin/publish.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     评论管理页面
"""


def commentManagerPage(request):
    return render(request, "admin/commentmanager.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     创建书籍页面
"""


def EditBookInfoPage(request):
    return render(request, "admin/check.html")


def UploadImgPage(request):
    return render(request, "admin/uploadimg.html")

def SuccessPage(request):
    return render(request, "admin/success.html")



# class AlipayAPIView(APIView):
#
#     def get(self, request):
#         alipay = Alipay(pid='2088122952530975', key='2017041506742165', seller_email='616254086@qq.com')
#         out_trade_no =
#         subject =
#         total_fee =
#         return_url =
#         notify_url =
#         url = alipay.create_direct_pay_by_user_url(out_trade_no='your_order_id', subject='your_order_subject', total_fee='100.0',
#             return_url='your_order_return_url', notify_url='your_order_notify_url')
#         print url
#         return HttpResponseRedirect(url)
