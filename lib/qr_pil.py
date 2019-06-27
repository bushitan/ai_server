#coding:utf-8
'''
	图片转pdf操作
	需要安装 reportlab，安装地址如下
	pip install reportlab -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
'''
from PIL import Image
import os
import re
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

class QRPrint():
	def __init__(self):
		self.base_path = r"image/"
		self.card_width = 591
		self.card_height = 1063
		self.space = 20
		self.space_left = 26 #基础28
		self.space_top = 128
		self.qr_x = 145
		self.qr_y = 643
		self.qr_width = 300 # 二维码宽度
		self.qr_height = 300 # 二维码高度


	# 获取打印的背景图
	# 不包含二维码
	# @param
	# 	bg_white	 A4空白背景
	# 	card_path 	 名片模板地址
	# 	template_out  A4模板输出地址
	def print_a4_template(self ,bg_white,card_path,template_out):
		bg_path = bg_white
		_card_path = card_path
		out = template_out
		im_bg = Image.open(bg_path)
		card = Image.open(_card_path)

		for i in range(0,4):
			_bx = (self.card_width + self.space) * i + self.space_left
			for j in range(0,3):
				_by = (self.card_height + self.space) * j + self.space_top
				im_bg.paste(card, (_bx, _by))
		im_bg.save(out)

	# 在已经打好的背景图上
	# 打印最终的二维码
	# @param
	# 	bg_path	 A4模板背景
	# 	qr_list  二维码列表
	# 	out_path 最终打印图片地址
	def print_a4_qr(self,bg_path,qr_list,out_path):
		bg = Image.open(bg_path)
		for i in range(0,4):
			_bx = (self.card_width + self.space) * i + self.space_left + self.qr_x
			for j in range(0,3):
				_by = (self.card_height + self.space) * j + self.space_top + self.qr_y

				if len(qr_list) <= 0 :
					break
				qr_path = qr_list.pop(0)  # 从第一个拿数据
				qr = Image.open(qr_path)  # 画qr
				qr = qr.resize((self.qr_width ,self.qr_height)) # 重新设置二维码大小
				bg.paste(qr, (_bx, _by ), mask=qr)
		bg.save(out_path)


	# 数组拆分
	def arr_size(self,arr,size):
		s=[]
		for i in range(0,int(len(arr))+1,size):
			c=arr[i:i+size]
			s.append(c)
		return s





# 二维码工具
class QRUtils():
	def __init__(self,bg_path = "",template_path = "",out_path = ""):
		self.qr_print = QRPrint()
		self.bg_path = bg_path
		self.template_path = template_path
		self.out_path = out_path

	# 输出打印模板
	# 可以正、反同时使用
	def create_bg(self):
		self.qr_print.print_a4_template(
			self.bg_path ,
			self.template_path ,
			self.out_path
		)

	# 开始打印图片
	def start(self,qr_list,final_path):
		self.create_bg()
		# self.create_print(qr_list,final_path)
		self.qr_print.print_a4_qr(self.out_path,qr_list,final_path)

	# 读取所有二维码地址
	# @param
	# 	all_qr_list 二维码地址数组
	def create_img(self,all_qr_list):
		_list = self.qr_print.arr_size(all_qr_list,12) # #将数组拆分为12
		# 将数组拆分为12长度的子数组
		for i, sub_list in enumerate( _list ):
			print (i,sub_list)
			self.start(sub_list , r"image/r_%s.jpg" % (i)) # 打印二维码


	# 读取所有二维码地址
	# @param
	# 	file_path 包含qr文件夹的地址
	def read_all_qr_path(self,file_path):
		qr_list = []
		for root, dirs, files in os.walk(file_path):
			files = sorted(files,key = lambda i:int(re.match(r'(\d+)',i).group())) #按名字排序
			for f in files:
				qr_list.append(root + f)
			return qr_list

if __name__ == "__main__":

	# 创建背面
	card_back =  QRUtils(
		bg_path = r"image/bg.jpg",
		template_path = r"image/card_back.jpg",
		out_path = r"image/r_card_back_template.jpg"
	)
	card_back.create_bg()

	card_front =  QRUtils(
		bg_path = r"image/bg.jpg",
		template_path = r"image/card_front.jpg",
		out_path = r"image/r_card_front_template.jpg"
	)
	card_front.create_bg()
	qr_list = card_front.read_all_qr_path(r"image/1_1_63/")
	card_front.create_img(qr_list)

	# print (qr_list)


	# print (card_front.create_pdf(qr_list))
	# card_front.start(qr_list , r"image/r_final1.jpg")




	# # 创建背面
	# card_back =  QRUtils(
	# 	bg_path = r"image/bg.jpg",
	# 	template_path = r"image/card_back.jpg",
	# 	out_path = r"image/r_card_back_template.jpg"
	# )
	# card_back.create_bg()
	#
	# # 创建正面模板
	# card_front =  QRUtils(
	# 	bg_path = r"image/bg.jpg",
	# 	template_path = r"image/card_front.jpg",
	# 	out_path = r"image/r_card_front_template.jpg"
	# )
	#
	# qr_list = []
	# for i in range(0,12):
	# 	qr_list.append( r"image/qr.png")
	# card_front.start(qr_list , r"image/r_final1.jpg")
