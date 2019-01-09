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
			'id':query_get.id,
			'name':query_get.name,
			'logo':query_get.logo,
			'cover':query_get.cover,
			'shop_time':query_get.shop_time,
			'phone':query_get.phone,
			'display_type':query_get.display_type,
			'content':query_get.content,
			'wx_content_url':query_get.wx_content_url,

			'latitude':query_get.poi.latitude,
			'longitude':query_get.poi.longitude,
			'address':query_get.poi.address,
			'postcode':query_get.poi.postcode,
			'category':query_get.poi.category,
			'boundary':query_get.poi.boundary,
			'panoinfo':query_get.poi.panoinfo,

			'group_name':query_get.group.name,
		}
		return _dict

	# 1 点击标签 —— 获取供求
	# def GetList(self):
	# 	_query = Image.objects.all()
	# 	return self._PackList(self._PackDict,_query)