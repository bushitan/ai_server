# -*- coding: utf-8 -*-
# from lite.query.group import *
# from lite.query.shop import *
import datetime
from lib.qi_niu import *

class ActionQiniu():
    def __init__(self):
        self.q = QiNiu()
    # self.qiniu = QiNiu()
    # self.query_group = QueryGroup()
    # self.query_shop = QueryShop()
    # g = self.query_group.Filter(id=1)


    def getToken(self):
        # filename ="ai_server_"  + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".jpg"
        filename = "ai_server_2019_02_03_16_10_41.jpg"
        token = self.q.getToken(filename)

        return token,filename


# import os,django
# django.setup()
# g = ActionSearch()
# print g.getShopListByGroupID(group_id=1)

