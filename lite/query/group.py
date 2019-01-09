# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
from django.db.models import Q
class QueryGroup(QueryBase):
	def __init__(self):
		super(QueryGroup,self).__init__(Group)
	def _PackDict(self,query_get):
		print query_get
		# _dict = {
		# 	'image_url':query_get.url,
		# 	'image_url':query_get.url,
		# }
		# return _dict

	# 1 点击标签 —— 获取供求
	# def GetList(self):
	# 	_query = Image.objects.all()
	# 	return self._PackList(self._PackDict,_query)