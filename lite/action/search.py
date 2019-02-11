# -*- coding: utf-8 -*-
from lite.query.group import *
from lite.query.shop import *

class ActionSearch():
	def __init__(self):
		self.query_group = QueryGroup()
		self.query_shop = QueryShop()
		# g = self.query_group.Filter(id=1)

	def getShopListByGroupID(self,*args, **kwargs):
		_group_id = kwargs["group_id"]
		return self.query_shop.Filter(group_id = _group_id)

# import os,django
# django.setup()
# g = ActionSearch()
# print g.getShopListByGroupID(group_id=1)