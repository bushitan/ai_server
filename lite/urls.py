# -*- coding: utf-8 -*-


from django.conf.urls import url
from lite.views import *



urlpatterns = [

    url(r'^search/shop/$', GetShopListByGroup.as_view()),

    # url(r'^my/example/$', MyExample.as_view()),

]