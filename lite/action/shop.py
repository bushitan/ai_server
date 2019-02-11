# -*- coding: utf-8 -*-
from lite.query.trace import *
from lite.query.shop import *
from lite.query.user import *

class ActionShop():
	def __init__(self):
		self.query_trace = QueryTrace()
		self.query_shop = QueryShop()
		self.query_user = QueryUser()
		# g = self.query_group.Filter(id=1)

	# 增加店铺
	def add(self,**kwargs):
		return self.query_shop.Add(**kwargs)

	# 删除店铺
	def delete(self,user_id,shop_id):
		print shop_id
		return self.query_shop.Delete(id = shop_id)

	# 修改店铺详情
	def update(self,user_id,shop_id,**kwargs):
		return self.query_shop.Update(shop_id,**kwargs)


	# 获取详情
	def getContent(self,shop_id):
		return self.query_shop.Get(id = shop_id)

	#获取自己的列表
	def getListBySelf(self,user_id):
		# 没有用户，返回空串
		return self.query_shop.filterShort(user_id = user_id)

	#获取自己的列表
	def getListByTrace(self,user_id):
		return self.query_trace.filterShort(user_id = user_id)


if __name__ == "__main__":
	import os,django
	django.setup()
	g = ActionShop()
	# print g.getContent(shop_id=1)
	# print g.getListBySelf(user_id=2)
	# print g.getListByTrace(user_id=2)
	# print g.updateShop(1,content=u"2sddfhsi7",title=u"标题1",user_id="1")
	print g.add(user_id=1,title="标题我的")
















