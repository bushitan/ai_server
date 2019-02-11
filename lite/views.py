#coding:utf-8
from django.http import HttpResponse
from django.views.generic import ListView
import json
from lib.message import *
from lib.util import *
from action.search import *
from action.qi_niu import *
from action.shop import *
from action.user import *
actionSearch = ActionSearch()
actionQiniu = ActionQiniu()
actionShop = ActionShop()
actionUser = ActionUser()


# 查询商铺
class GetShopListByGroup( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_group_id = request.GET.get('group_id',"")
			_shop_list = actionSearch.getShopListByGroupID( group_id = _group_id )
			_dict = {
				"shop_list":_shop_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

# 查询商铺
class QiniuGetToken( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _group_id = request.GET.get('group_id',"")
			# _shop_list = actionSearch.getShopListByGroupID( group_id = _group_id )
			token , key = actionQiniu.getToken()
			_dict = {
				"uptoken":token,
				"key":key,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )



# 用户登录
class UserLogin( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			code = request.GET.get('code',"")
			user_id = request.GET.get('user_id',"")
			_dict = {
				"user":actionUser.checkSession(code,user_id),
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )



# 查询商铺
class ShopAdd( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			user_id = request.GET.get('user_id',"")
			shop_id = request.GET.get('shop_id',"")
			detail = {
				'cover' : request.GET.get('cover',""), #封面
				'name' : request.GET.get('name',""),	#名称
				'title' : request.GET.get('title',""), #标题
				'summary' : request.GET.get('summary',""),#概述
				'content' : request.GET.get('content',""),#内容详情
				'address' : request.GET.get('address',""),#地址
				# 'latitude' : int( request.GET.get('latitude',0)),#纬度
				# 'longitude' :int( request.GET.get('longitude',0)),#经度
				'latitude' :0,#纬度
				'longitude' :0#经度
			}

			if shop_id == '': #增加新店铺
				detail["user_id"] = user_id
				actionShop.add(**detail)
				msg = u"增加店铺成功"
			else: #修改已有店铺
				actionShop.update(user_id,shop_id,**detail)
				msg = u"更新店铺详情成功"
			_dict = {
				"msg":msg,
				"shop_list":actionShop.getListBySelf(user_id),
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )



# 查询商铺
class ShopDelete( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			user_id = request.GET.get('user_id',"")
			shop_id = request.GET.get('shop_id',"")
			actionShop.delete(user_id,shop_id)
			print (user_id,shop_id)
			_dict = {
				"msg":u"删除店铺成功",
				"shop_list":actionShop.getListBySelf(user_id),
				# "msg":u"更新店铺详情成功",
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )



# 店铺详情
class ShopGet( ListView):
	def get(self, request, *args, **kwargs):
		try:
			shop_id = request.GET.get('shop_id',"")
			_dict = {
				"shop":actionShop.getContent(shop_id),
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

# 用户本身的店铺
class ShopGetListByUser( ListView):
	def get(self, request, *args, **kwargs):
		try:
			user_id = request.GET.get('user_id',"")
			_dict = {
				"shop_list":actionShop.getListBySelf(user_id),
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

# 用户浏览记录
class ShopGetTraceByUser( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			user_id = request.GET.get('user_id',"")
			_dict = {
				"shop_list":actionShop.getListByTrace(user_id),
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
