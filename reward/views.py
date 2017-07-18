# **coding: utf-8**
import json
from rest_framework.views import APIView
from utils import shortcuts
from django.http import HttpResponse, QueryDict
from .models import Reward
from .serializers import RewardSerializers
from account.decorators import login_required
from books.models import BookInfo
from utils import rewardtype

"""
    Author:	         毛毛
    Version:         0.02v
    Date:            2017/03/30
    Description:     打赏信息模型
    request:
       字段名称     bookId    　productionNumber     rewardType
       描述　　     书籍id     　   物品数量　            打赏类型

"""


class RewardViewAPI(APIView):

    @ login_required
    def get(self, request):
        # serializer = RewardSerializers(request.data)
        userId = request.user.id
        userName = request.user.userName
        bookId = request.GET.get("bookId")
        productionNumber = request.GET.get("productionNumber")
        rewardType = request.GET.get("rewardType")
        book = BookInfo.objects.filter(id=bookId).get()
        rewardMoney =rewardtype.rewardType[rewardType].money * int(productionNumber)
        reward = Reward(userId=userId, bookId=bookId, userName=userName, bookName=book.bookName,
                        rewardMoney=rewardMoney, productionNumber=productionNumber, rewardType=rewardType)
        reward.save()
        message = "打赏成功"
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
        字段名称    userName        rewardType       productionNumber
        描述       打赏人姓名　        打赏类型        　   打赏数量
"""


class RewardBookViewAPI(APIView):
    def get(self, request):
        bookId = request.GET['bookId']
        book = Reward.objects.filter(bookId=bookId).all()
        book_reward = RewardSerializers(book, many=True)
        reward = QueryDict(mutable=True)
        reward['record'] = book_reward.data
        return HttpResponse(json.dumps(reward.dict()))


"""
    Author:	         毛毛
    Version:         0.02v
    Date:            2017/03/30
    Description:     书籍评论在个人中心显示接口
    request:
        字段名称     userId     commentNumber
        描述        用户Id      请求条数
    response:
        字段名称    bookName    rewardTime     rewardType       productionNumber
        描述       书籍名称　  　时间            打赏类型        打赏数量
"""


class RewardUserViewAPI(APIView):
    def post(self, request):
        return HttpResponse()