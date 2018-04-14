from django.http import HttpResponse
from django.urls import path
from . import views


# 定义命令空间，避免多app导致url相同的问题
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]