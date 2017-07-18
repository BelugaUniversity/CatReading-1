from .models import DayDataStatistics, MonthDataStatistics

def dayDataStatistics():
    dayData = DayDataStatistics()
    dayData.save()


def MonthDataStatistics():
    monthData = MonthDataStatistics()
    monthData.save()