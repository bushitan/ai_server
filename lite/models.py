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

class POI(BaseModel):
	name =  models.CharField(max_length=32, verbose_name=u'名称',default="",null=True,blank=True)
	type =  models.IntegerField(u'类型',default=POT_TYPE_NORMAL,choices=POT_TYPE.items())
	latitude =  models.FloatField(max_length=100, verbose_name=u'纬度',default="",null=True,blank=True)
	longitude =  models.FloatField(max_length=100, verbose_name=u'经度',default="",null=True,blank=True)
	phone =  models.CharField(max_length=32, verbose_name=u'电话',default="",null=True,blank=True)
	address =  models.CharField(max_length=50, verbose_name=u'地址',default="",null=True,blank=True)
	postcode =  models.CharField(max_length=32, verbose_name=u'邮政编码',default="",null=True,blank=True)
	category =  models.CharField(max_length=32, verbose_name=u'目类',default="",null=True,blank=True)
	boundary =  models.CharField(max_length=32, verbose_name=u'范围',default="",null=True,blank=True)
	panoinfo =  models.CharField(max_length=100, verbose_name=u'信息',default="",null=True,blank=True)
	class Meta:
		verbose_name_plural = verbose_name = u'POI'
	def __unicode__(self):
		return '%s' % (self.name)



class Shop(BaseModel):
	name =  models.CharField(max_length=32, verbose_name=u'店铺名称',default="",null=True,blank=True)
	poi =  models.ForeignKey( POI,verbose_name=u'对应poi点')
	group =  models.ForeignKey( Group,verbose_name=u'所属group群组')
	logo =  models.CharField(max_length=500, verbose_name=u'logo',default="",null=True,blank=True)
	cover =  models.CharField(max_length=500, verbose_name=u'封面图',default="",null=True,blank=True)
	shop_time =  models.CharField(max_length=32, verbose_name=u'营业时间',default="",null=True,blank=True)
	phone =  models.CharField(max_length=32, verbose_name=u'电话',default="",null=True,blank=True)
	display_type =  models.IntegerField(u'展示方式',default=DISPLAY_TYPE_WX_URL,choices=DISPLAY_TYPE.items())
	content =  models.TextField( verbose_name=u'展示内容',default="",null=True,blank=True)
	wx_content_url =  models.CharField(max_length=500, verbose_name=u'微信展示链接',default="",null=True,blank=True)
	class Meta:
		verbose_name_plural = verbose_name = u'店铺'
	def __unicode__(self):
		return '%s' % (self.name)

