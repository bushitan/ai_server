#coding:utf-8
from PIL import Image


class QRPrint():
	def __init__(self):
		self.base_path = r"image/"
		self.card_width = 591
		self.card_height = 1063
		self.space = 20
		self.space_left = 28
		self.space_top = 128
		self.qr_x = 145
		self.qr_y = 643

	# 获取打印的背景图
	# 不包含二维码
	def start_base(self ,bg_white,card_path,template_out):
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
	def start_final(self,bg_path,qr_list,out_path):
		bg = Image.open(bg_path)
		for i in range(0,4):
			_bx = (self.card_width + self.space) * i + self.space_left + self.qr_x
			for j in range(0,3):
				_by = (self.card_height + self.space) * j + self.space_top + self.qr_y

				if len(qr_list) <= 0 :
					break
				qr_path = qr_list.pop(0)  # 从第一个拿数据
				qr = Image.open(qr_path)  # 画qr
				bg.paste(qr, (_bx, _by), mask=qr)
		bg.save(out_path)


class QRUtils():
	def __init__(self,bg_path,template_path,out_path):
		self.qr_print = QRPrint()
		self.bg_path = bg_path
		self.template_path = template_path
		self.out_path = out_path

	# 输出打印模板
	# 可以正、反同时使用
	def create_bg(self):
		self.qr_print.start_base(
			self.bg_path ,
			self.template_path ,
			self.out_path
		)

	# 倒霉
	def create_print(self,qr_list ,final_path):
		self.qr_print.start_final(self.out_path,qr_list,final_path)

	def start(self,qr_list,final_path):
		self.create_bg()
		self.create_print(qr_list,final_path)

if __name__ == "__main__":


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

	qr_list = []
	for i in range(0,12):
		qr_list.append( r"image/qr.png")
	card_front.start(qr_list , r"image/r_final1.jpg")
