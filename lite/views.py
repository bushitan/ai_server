#coding:utf-8
from django.http import HttpResponse
from django.views.generic import ListView
import json
from lib.message import *
from lib.util import *
from action.search import *
actionSearch = ActionSearch()


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
