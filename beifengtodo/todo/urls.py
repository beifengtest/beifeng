#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: urls.py
@time: 2015/12/30 0030 下午 12:32
"""

from django.conf.urls import url
from todo.views import *

urlpatterns = [url(r'^$',index,name='index'),
               url(r'^(\d*)/$',getTodo,name='gettodo'),
               # url(r'^(?P<todoid>\d*)/$',getTodo,name='gettodo2')
              ]
