# -*- coding: utf-8 -*-
from django.contrib import admin
from lite.models import *



# class POIAdmin(admin.ModelAdmin):
# 	list_display = ('id','name','type','latitude','longitude','phone','address','postcode','category','boundary','panoinfo',)
# 	# list_display = ('name','type','latitude','longitude','phone','address','postcode','category','boundary','panoinfo',)
# 	fieldsets = (
#      (u"名称", {'fields': ['name','type',]}),
#       (u"坐标", {'fields': ['latitude','longitude',]}),
#       (u"附加信息", {'fields': ['phone','address','postcode','category','boundary','panoinfo',]}),
#     )
# 	search_fields = ('id','name',) #右边过滤器
# admin.site.register(POI,POIAdmin)



class GroupAdmin(admin.ModelAdmin):
	list_display = ('id','name','mode','keyword','qr_url',)
	fieldsets = (
		(u"名称", {'fields': ['name',]}),
		(u"查询内容", {'fields': ['mode','keyword']}),
		(u"二维码", {'fields': ['qr_url',]}),
    )
	search_fields = ('id','name',)
admin.site.register(Group,GroupAdmin)



class ShopAdmin(admin.ModelAdmin):
	list_display = ('id','cover','name','title','summary','address','latitude','longitude',)
	# list_filter = ('name','poi','group','logo','cover','shop_time','display_type','content','wx_content_url',)
	fieldsets = (
		(u"名称", {'fields': ['user','name',]}),
      	(u"显示", {'fields': ['title','summary','cover',]}),
      	(u"坐标", {'fields': ['address','latitude','longitude','content',]}),
		# (u"店铺展示", {'fields': ['display_type','wx_content_url','content',]}),
		# (u"店铺信息", {'fields': ['shop_time','phone',]}),
    )
	search_fields = ('id','name','group',)
	raw_id_fields = ('group',)
admin.site.register(Shop,ShopAdmin)


class UserAdmin(admin.ModelAdmin):
	pass
admin.site.register(User,UserAdmin)
class TraceAdmin(admin.ModelAdmin):
	pass
admin.site.register(Trace,TraceAdmin)

