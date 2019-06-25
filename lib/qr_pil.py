#coding:utf-8
from PIL import Image


class QRPrint():
	def __init__(self):
		self.base_path = r"image/"
		pass

	def create_page(self):
		newIm= Image.new('RGBA', (100, 100), 'red')
		newIm.save(self.base_path  + r'1.png')

	def copy(self,bg_path ,qr_path,x,y):
		im_bg = Image.open(bg_path)
		qr = Image.open(qr_path)
		# cropedIm = im.crop((100,100,200,200))
		im_bg.paste(qr, (x, y), mask=qr)
		# im_bg.show()
		im_bg.save(self.base_path + r'paste.jpg')
	def start(self):
		bg = self.base_path  + r'bg.jpg'
		qr = self.base_path  + r'wm_2UdX86fZ_200.png'
		self.copy(bg,qr,68,601)

if __name__ == "__main__":
	q = QRPrint()
	q.create_page()
	q.start()


# 2468  617
# 3496  874

# 620 877

# 二维码位置  x=68 , y=601   w=200, h=200



#
#
# im_path = r'image/mp.jpg'
# im = Image.open(im_path)
# width, height = im.size
# # 宽高
# print(im.size, width, height)
# # 格式，以及格式的详细描述
# print(im.format, im.format_description)
#
# im.save(r'image/mp1.jpg')
# im.show()
