# -*- coding: utf-8 -*-


from django.conf.urls import url
from lite.views import *



urlpatterns = [

    url(r'^search/shop/$', GetShopListByGroup.as_view()),


    url(r'^user/login/$', UserLogin.as_view()), #增加店铺

    url(r'^shop/add/$', ShopAdd.as_view()), #增加 or 更新店铺
    url(r'^shop/delete/$', ShopDelete.as_view()), #删除店铺
    url(r'^shop/get/$', ShopGet.as_view()), #查店铺详情
    url(r'^shop/list/$', ShopGetListByUser.as_view()), #查询店铺列表
    url(r'^shop/list/search/$', ShopGetListBySearch.as_view()), #查询店铺列表
    url(r'^shop/trace/$', ShopGetTraceByUser.as_view()), #用户浏览记录 ( 包含 增加、删除）


    url(r'^qiniu/token/$', QiniuGetToken.as_view()), #获取token


    # url(r'^my/example/$', MyExample.as_view()),

]