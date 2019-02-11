#coding:utf-8
from django.db import models

from lib.util import *
import django.utils.timezone as timezone


class BaseModel(models.Model):

	class Meta:
		abstract = True


class Group(BaseModel):
	name = models.CharField(max_length=100, verbose_name=u'名称',default="",null=True,blank=True)
	mode = models.IntegerField(u'搜索模式',default=GROUP_MODE_ID,choices=GROUP_MODE.items())
	keyword = models.CharField(max_length=100, verbose_name=u'关键字',default="",null=True,blank=True)
	qr_url = models.CharField(max_length=100, verbose_name=u'二维码链接',default="",null=True,blank=True)

	class Meta:
		verbose_name_plural = verbose_name = u'群组'
	def __unicode__(self):
		return '%s' % (self.name)


class User(BaseModel):
	name =  models.CharField(max_length=100, verbose_name=u'姓名',default="",null=True,blank=True)
	# userInfo
	nick_name =  models.CharField(max_length=100, verbose_name=u'昵称',null=True,blank=True)
	avatar_url =  models.CharField(max_length=100, verbose_name=u'头像',null=True,blank=True)
	gender =  models.CharField(max_length=100, verbose_name=u'性别',null=True,blank=True)
	city =  models.CharField(max_length=100, verbose_name=u'城市',null=True,blank=True)
	province =  models.CharField(max_length=100, verbose_name=u'省份',null=True,blank=True)
	country =  models.CharField(max_length=100, verbose_name=u'国家',null=True,blank=True)
	# login
	wx_open_id = models.CharField(max_length=50, verbose_name=u'微信OpenID',null=True,blank=True)
	wx_session_key = models.CharField( max_length=128,verbose_name=u'微信SessionKey',null=True,blank=True)
	wx_union_id = models.CharField(max_length=50, verbose_name=u'微信UnionID',null=True,blank=True)

	class Meta:
		verbose_name_plural = verbose_name = u'用户'
	def __unicode__(self):
		return '%s' % (self.name)

class Shop(BaseModel):
	name =  models.CharField(max_length=32, verbose_name=u'店铺名称',default="",null=True,blank=True)
	# poi =  models.ForeignKey( POI,verbose_name=u'对应poi点')
	group =  models.ForeignKey( Group,verbose_name=u'所属group群组',null=True,blank=True)
	user =  models.ForeignKey( User,verbose_name=u'所属用户',null=True,blank=True)
	title =  models.CharField(max_length=32, verbose_name=u'标题',default="",null=True,blank=True)
	summary =  models.CharField(max_length=32, verbose_name=u'简介',default="",null=True,blank=True)
	logo =  models.CharField(max_length=500, verbose_name=u'logo',default="",null=True,blank=True)
	cover =  models.CharField(max_length=500, verbose_name=u'封面图',default="",null=True,blank=True)
	content =  models.TextField( verbose_name=u'展示内容',default="",null=True,blank=True)
	shop_time =  models.CharField(max_length=32, verbose_name=u'营业时间',default="",null=True,blank=True)
	display_type =  models.IntegerField(u'展示方式',default=DISPLAY_TYPE_WX_URL,choices=DISPLAY_TYPE.items())
	wx_content_url =  models.CharField(max_length=500, verbose_name=u'微信展示链接',default="",null=True,blank=True)

	type =  models.IntegerField(u'类型',default=POT_TYPE_NORMAL,choices=POT_TYPE.items())
	latitude =  models.FloatField(max_length=100, verbose_name=u'纬度',default=0,null=True,blank=True)
	longitude =  models.FloatField(max_length=100, verbose_name=u'经度',default=0,null=True,blank=True)
	phone =  models.CharField(max_length=32, verbose_name=u'电话',default="",null=True,blank=True)
	address =  models.CharField(max_length=50, verbose_name=u'地址',default="",null=True,blank=True)
	postcode =  models.CharField(max_length=32, verbose_name=u'邮政编码',default="",null=True,blank=True)
	category =  models.CharField(max_length=32, verbose_name=u'目类',default="",null=True,blank=True)
	boundary =  models.CharField(max_length=32, verbose_name=u'范围',default="",null=True,blank=True)
	panoinfo =  models.CharField(max_length=100, verbose_name=u'信息',default="",null=True,blank=True)

	date =  models.CharField(max_length=100, verbose_name=u'信息',default="",null=True,blank=True)
	# time =  models.CharField(max_length=100, verbose_name=u'信息',default="",null=True,blank=True)

	class Meta:
		verbose_name_plural = verbose_name = u'店铺'
	def __unicode__(self):
		return '%s' % (self.name)


class Trace(BaseModel):
	user =  models.ForeignKey( User,verbose_name=u'用户')
	shop =  models.ForeignKey( Shop,verbose_name=u'店铺')

	class Meta:
		verbose_name_plural = verbose_name = u'浏览记录'
	def __unicode__(self):
		return '%s' % (self.id)
















