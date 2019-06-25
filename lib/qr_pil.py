#coding:utf-8
from PIL import Image


class QRPrint():
	def __init__(self):
		self.base_path = r"image/"
		pass

	def create_page(self):
		newIm= Image.new('RGB', (100, 100), 'red')
		newIm.save(self.base_path  + r'1.png')

	def copy(self,bg_path ,qr_path):
		im_bg = Image.open(bg_path)
		im = Image.open(qr_path)
		# cropedIm = im.crop((100,100,200,200))
		im_bg.paste(im, (0, 0))
		im_bg.show()
		im_bg.save(self.base_path + r'paste.jpg')
	def start(self):
		bg = self.base_path  + r'mp.jpg'
		qr = self.base_path  + r'wm.jpg'
		self.copy(bg,qr)

if __name__ == "__main__":
	q = QRPrint()
	q.create_page()
	q.start()

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
