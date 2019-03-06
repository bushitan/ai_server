# -*- coding: utf-8 -*-
import xlrd
import jieba
import json
import xlwt

workbook = xlrd.open_workbook(r'1.xlsx')
sheet_names= workbook.sheet_names()
# sheet2 = sheet_names[0]
sheet2 = workbook.sheet_by_name(sheet_names[0])
nrows = sheet2.nrows

def cut(word):
	return jieba.lcut(word, cut_all=False)
def to_json(row):
	return{
		'title':cut(row[0]),
		'content':cut(row[3]),
		'collect':row[5],
		'comment':row[6],
		'star':row[7],
		'count':row[8],
	}

def write_file(data_dict):
	name ="data_red/1.txt"
	with open(name,"w") as f:
		json.dump(data_dict,f)

def read_file():
	with open("data_red/1.txt",'r') as load_f:
		load_dict = json.load(load_f)
		return load_dict

def main():
	# r = sheet2.row_values(2)
	_list = []
	for i in range(2,2010):
		print(sheet2.row_values(i))
		col = sheet2.row_values(i)
		_list.append( to_json(col) )

	write_file({
		"list":_list
	})
# main()
def write_excel(counts):
	wbk = xlwt.Workbook()
	sheet = wbk.add_sheet('sheet 1')

	items = list(counts.items())
	items.sort(key=lambda x:x[1], reverse=True)
	for i in range(0,len(items)):
		word, count = items[i]
		# print word.encode('GBK', 'ignore'),count
		sheet.write(i,1,word)#第0行第一列写入内容
		sheet.write(i,2,count)#第0行第一列写入内容

	wbk.save('content.xls')

def read():
	counts = {}
	_file = read_file()
	_list = _file['list']
	for i in _list:
		_title =i['content']
		for word in _title:
			counts[word] = counts.get(word,0) + 1
	write_excel(counts)
	# items = list(counts.items())
	# items.sort(key=lambda x:x[1], reverse=True)
	# for i in range(0,len(items)):
	# 	word, count = items[i]
	# 	print word.encode('GBK', 'ignore'),count


read()


# for i in sheet2.row_values(1):
# 	print i.encode('GBK', 'ignore')
# for i in range(nrows):
# 	print(sheet2.row_values(i))


# for sheet_name in sheet_names:
#
# 　　 sheet2 = workbook.sheet_by_name(sheet_name)
#
# 　　 print sheet_name rows = sheet2.row_values(3) # 获取第四行内容
#
# 　　 cols = sheet2.col_values(1) # 获取第二列内容
#
# 　　 print rows
#
# 　　 print cols