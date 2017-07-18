# **coding: utf-8**
import json
from rest_framework.views import APIView
from utils import shortcuts
from django.http import HttpResponse, QueryDict
from .models import Comment
from books.models import BookInfo
from django.core.paginator import Paginator
from .serializers import CommentSerializers, CommentManagerSerializers
from account.decorators import login_required

"""
    Author:	         毛毛
    Version:         0.02v
    Date:            2017/05/01
    Description:     提交评论接口
    request:
       字段名称     bookId   commentTitle    commentContent
       描述　　     书籍id      评论标题           评论内容
"""


class CommentViewAPI(APIView):

    @ login_required
    def get(self, request):
        userId = request.user.id
        userName = request.user.userName
        bookId = request.GET.get("bookId")
        commentTitle = request.GET.get("commentTitle")
        commentContent = request.GET.get("commentContent")
        book = BookInfo.objects.filter(id=bookId).get()
        comment = Comment(userId=userId, bookId=bookId, userName=userName,  bookName=book.bookName, commentTitle=commentTitle, commentContent=commentContent)
        comment.save()
        message = "评论成功"
        return shortcuts.success_response(message)


"""
    Author:	         毛毛
    Version:         0.02v
    Date:            2017/03/30
    Description:     书籍评论在详情页显示接口
    request:
        字段名称     bookId
        描述        书籍Id
    response:
        字段名称    userName    commentTime     commentContent
        描述       评论人姓名　  时间             内容
"""


class CommentBookViewAPI(APIView):

    def get(self, request):
        bookId = request.GET['bookId']
        book = Comment.objects.filter(bookId=bookId).filter(isShow=False).all()[0:3]
        book_comment = CommentSerializers(book, many=True)
        comment = QueryDict(mutable=True)
        comment['bookComment'] = book_comment.data
        return HttpResponse(json.dumps(comment.dict()))


"""
    Author:	         毛毛
    Version:         0.02v
    Date:            2017/03/30
    Description:     书籍评论在个人中心显示接口
    request:
        字段名称     userId     commentNumber
        描述        用户Id      请求条数
    response:
        字段名称    bookName    commentTime     commentContent
        描述       评论人姓名　  时间             内容
"""


class CommentUserViewAPI(APIView):

    def get(self, request):
        bookId = request.GET['Id']
        book = Comment.objects.filter(bookId=bookId).all()
        book_comment = CommentSerializers(book, many=True)
        comment = QueryDict(mutable=True)
        comment['userComment'] = book_comment.data
        return HttpResponse(json.dumps(comment.dict()))


"""
    Author:	         毛毛
    Version:         0.02v
    Date:            2017/05/21
    Description:     书籍评论在个人中心显示接口
    request:
        字段名称     userId     commentNumber
        描述        用户Id      请求条数
    response:
        字段名称    bookName    commentTime     commentContent
        描述       评论人姓名　  时间             内容
"""


class CommentManagerViewAPI(APIView):

    def get(self, request):
        bookId = request.GET['bookId']
        numPage = request.GET['numPage']
        book = BookInfo.objects.get(id=bookId)
        comments = Comment.objects.filter(bookId=bookId).all()
        paginator = Paginator(comments, 10)
        commentManagerSerializers = CommentManagerSerializers(paginator.page(numPage), many=True)
        comment = QueryDict(mutable=True)
        comment['commentManagerItems'] = commentManagerSerializers.data
        comment['bookName'] = book.bookName
        comment['pageNumber'] = paginator.num_pages
        return HttpResponse(json.dumps(comment.dict()))


class EditCommentManagerViewAPI(APIView):

    def get(self, request):

        commentId = request.GET["commentId"]
        isShow = request.GET["isShow"]
        commentStick = request.GET["commentStick"]
        commentEssence = request.GET["commentEssence"]
        comment = Comment.objects.get(id=commentId)

        print commentStick
        print commentEssence

        type = 0

        if ('true' == commentStick) and ('true' == commentEssence):
            type = 3
            commentStick = True
            commentEssence = True

        if ('false' == commentStick) and ('true' == commentEssence):
            type = 2
            commentStick = False
            commentEssence = True

        if ('true' == commentStick) and ('false' == commentEssence):
            type = 1
            commentStick = True
            commentEssence = False

        if ('false' == commentStick) and ('false' == commentEssence):
            type = 0
            commentStick = False
            commentEssence = False

        if ('true' == isShow):
            isShow = True
        else:
            isShow = False

        comment.commentType = type
        print type
        comment.save()

        comment.commentStick = commentStick
        comment.commentEssence = commentEssence
        comment.isShow = isShow
        comment.save()
        message = "评论状态修改成功"
        return shortcuts.success_response(message)