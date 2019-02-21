# -*- coding: utf-8 -*-
from weixin import WeixinLogin
AII_ID_ZHAO_DD = 'wxd2f409241725502b'
AII_ID_COFFEE = 'wx7500cd1b23a33998'
login_zhaodd = WeixinLogin(AII_ID_ZHAO_DD, '986104a41ccaa0a5c25c253010277c56') #找店店
login_coffee = WeixinLogin(AII_ID_COFFEE, '3208c7e9928ad7d75215317bc24cf722') #咖啡小地图
# data = login.jscode2session("071znnjl1iGk6o0nPvml1Lvyjl1znnjf")
# print data


# -*- coding: utf-8 -*-
from lite.query.user import *
# from lite.query.shop import *

class ActionUser():
	def __init__(self):
		self.query_user = QueryUser()

	def checkSession(self,app_id,code,user_id):
		# print code,user_id
		if user_id == "" or self.query_user.IsExists(id = user_id) == False:
			print 123
			data = self.getLogin(app_id,code)
			print data
			return self._checkUser(data) # 新用户存入

		return self.query_user.Get(id = user_id)

	#
	def getLogin(self,app_id,code):
		if app_id == AII_ID_ZHAO_DD:
			return login_zhaodd.jscode2session(code)
		if app_id == AII_ID_COFFEE:
			return login_coffee.jscode2session(code)
		raise( 'APP_ID is null')

	# 检测用户是否存在
	def _checkUser(self,data):
		open_id = data['openid']
		session_key = data['session_key']
		unionid = data['unionid']

		if self.query_user.IsExists(wx_union_id = unionid) is True: #用户已存在，查询
			return self.query_user.Get(wx_union_id = unionid)
		else: # 用户不存在，新增
			return self.query_user.Add(
				wx_open_id = open_id,
				wx_session_key = session_key,
				wx_union_id = unionid,
			)