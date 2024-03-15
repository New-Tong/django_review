# _*_ coding : utf-8 _*_
# @time : 2024/03/15 13:30
# @author : 牛童
# @File : urls.py
# @Project : review_bookmanager
from django.urls import path

from book.views import index

urlpatterns = [
    path('home/', index),
]
