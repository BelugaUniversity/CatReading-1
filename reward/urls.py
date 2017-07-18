import views
from django.conf.urls import url

urlpatterns = [
    url(r'RewardViewAPI/', views.RewardViewAPI.as_view()),
    url(r'^RewardViewAPI/', views.RewardBookViewAPI.as_view()),
    url(r'^RewardViewAPI/', views.RewardUserViewAPI.as_view()),
]
