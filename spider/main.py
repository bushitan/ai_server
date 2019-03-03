# -*- coding: utf-8 -*-
# import  sys ,io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
import json
from data.wxc_6flood import *
comment_json = json.loads( comment[0])
# print  comment_json['data']['comments']
content_list = []
for com in comment:
    c_json = json.loads(com)
    print c_json
    list = c_json['data']['comments']
    for i in list:
        content_list.append(
             i['content'].encode('GBK', 'ignore')
        )

print content_list