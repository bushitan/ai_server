# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
from django.db.models import Q
class QueryTrace(QueryBase):
	def __init__(self):
		super(QueryTrace,self).__init__(Trace)
	def _PackDict(self,query_get):
		# print query_get
		_dict = {
			'id':query_get.id,
			'shop_id':query_get.shop_id,
			'cover':query_get.shop.cover,
			'summary':query_get.shop.summary,
			'user_id':query_get.user_id,
		}
		return _dict

	def filterShort(self,user_id):
		trace_list = Trace.objects.filter(user_id = user_id)
		list = []
		for t in trace_list:
			list.append({
				'shop_id':t.shop.id,
				"cover": t.shop.cover,
				"title": t.shop.title,
				"summary": t.shop.summary,
				"address": t.shop.address,
			})
		return  list

if __name__ == "__main__":
	import os,django
	django.setup()
	uid = 2
	trace_list = Trace.objects.filter(user_id = uid)
	list = []
	for t in trace_list:
		list.append({
			"cover": t.shop.cover,
			"title": t.shop.title,
			"summary": t.shop.summary,
		})
	print list
