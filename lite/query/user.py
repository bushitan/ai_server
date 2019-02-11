# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
from django.db.models import Q
class QueryUser(QueryBase):
	def __init__(self):
		super(QueryUser,self).__init__(User)
	def _PackDict(self,query_get):
		# print query_get
		_dict = {
			'id':query_get.id,
			'name':query_get.name,
			'nick_name':query_get.nick_name,
			'avatar_url':query_get.avatar_url,
			'gender':query_get.gender,
			'city':query_get.city,
			'province':query_get.province,
			'country':query_get.country,

			'wx_open_id':query_get.wx_open_id,
			'wx_session_key':query_get.wx_session_key,
			'wx_union_id':query_get.wx_union_id,

		}
		return _dict

	# 1 点击标签 —— 获取供求
	# def GetList(self):
	# 	_query = Image.objects.all()
	# 	return self._PackList(self._PackDict,_query)