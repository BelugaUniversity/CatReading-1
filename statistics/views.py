from django.shortcuts import render
import json
from django.http import QueryDict, HttpResponse
from rest_framework.views import APIView
from django.core.paginator import Paginator
from .serializers import DayDataStatisticsSerializers, MonthDataStatisticsSerializers, LineCharDataStatisticsSerializers
from .models import DayDataStatistics, MonthDataStatistics, TotalPVNumber, TotalLogonNumber, TotalRewardNumber, PropsNumber
# Create your views here.

class DataStaticsAPIView(APIView):
    def get(self, request):
        dayDataNumPage = request.GET['dayDataNumPage']
        monthDataNumPage = request.GET['monthDataNumPage']
        dayData = DayDataStatistics.objects.all()
        monthData = MonthDataStatistics.objects.all()
        lineCharData = DayDataStatistics.objects.all().order_by('-produceDataDate')[0:7]
        dayDataPaginator = Paginator(dayData, 10)
        monthDataPaginator = Paginator(monthData, 10)
        dayDataSerializers = DayDataStatisticsSerializers(dayDataPaginator.page(dayDataNumPage).object_list, many=True)
        monthDataSerializers = MonthDataStatisticsSerializers(monthDataPaginator.page(monthDataNumPage).object_list, many=True)
        lineCharDataSerializers = LineCharDataStatisticsSerializers(lineCharData, many=True)
        dataStatics = QueryDict(mutable=True)
        dataStatics['dayDataPageNumber'] = dayDataPaginator.num_pages
        dataStatics['monthDataPageNumber'] = monthDataPaginator.num_pages
        dataStatics['dayData'] = dayDataSerializers.data
        dataStatics['monthData'] = monthDataSerializers.data
        dataStatics['lineCharData'] = lineCharDataSerializers.data
        dataStatics['TotalPVNumber'] = TotalPVNumber()
        dataStatics['TotalLogonNumber'] = TotalLogonNumber()
        dataStatics['TotalRewardNumber'] = TotalRewardNumber()
        dataStatics['TotalCatBallNumber'] = PropsNumber(1)
        dataStatics['TotalCatnipNumber'] = PropsNumber(2)
        dataStatics['TotalCatStickNumber'] = PropsNumber(3)
        dataStatics['TotalCatFoodNumber'] = PropsNumber(4)
        dataStatics['TotalCatFishNumber'] = PropsNumber(5)
        dataStatics['TotalCatHouseNumber'] = PropsNumber(6)
        return HttpResponse(json.dumps(dataStatics.dict()))
