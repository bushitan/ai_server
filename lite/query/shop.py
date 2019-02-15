# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
from django.db.models import Q
class QueryShop(QueryBase):
	def __init__(self):
		super(QueryShop,self).__init__(Shop)
	def _PackDict(self,query_get):
		# print query_get
		_dict = {
			'shop_id':query_get.id,
			'cover':query_get.cover,
			'name':query_get.name,
			'title':query_get.title,
			'summary':query_get.summary,
			'content':query_get.content,
			'address':query_get.address,
			'latitude':query_get.latitude,
			'longitude':query_get.longitude,

            #
			# 'group_id':query_get.group_id,
			# 'user_id':query_get.user_id,
			# 'logo':query_get.logo,
			# 'shop_time':query_get.shop_time,
			# 'display_type':query_get.display_type,
			# 'content':query_get.content,
			# 'wx_content_url':query_get.wx_content_url,
            #
			# 'latitude':query_get.latitude,
			# 'longitude':query_get.longitude,
			# 'phone':query_get.phone,
			# 'address':query_get.address,
			# 'postcode':query_get.postcode,
			# 'category':query_get.category,
			# 'boundary':query_get.boundary,
			# 'panoinfo':query_get.panoinfo,

			# 'group_name':query_get.group.name,
		}
		return _dict

	# 打包要展示的内容
	def _packDisplay(self,query_get):
		_dict = {
			'shop_id':query_get.id,
			'user_id':query_get.user_id,
			'name':query_get.name,
			'title':query_get.title,
			'summary':query_get.summary,
			'cover':query_get.cover,
			'address':query_get.address,
			'latitude':query_get.latitude,
			'longitude':query_get.longitude,
		}
		return _dict

	# 获取查询内容
	def filterShort(self,user_id):
		_shop_list = Shop.objects.filter(user_id = user_id)
		return self._PackList( self._packDisplay,_shop_list)

	# 更新
	def Update(self,shop_id,**kwargs):
		_shop_list = Shop.objects.filter(id = shop_id).update(**kwargs)
		return _shop_list

	# 1 点击标签 —— 获取供求
	# def GetList(self):
	# 	_query = Image.objects.all()
	# 	return self._PackList(self._PackDict,_query)