# -*- coding: utf-8 -*-
# import qiniu
import qiniu

# 七牛配置
QINIU_ACCESS_KEY = 'bK5xWj0a-TBIljlxHYOHuQib9HYF_9Ft-HtP8tEb'
QINIU_SECRET_KEY = '56lucORYc45sF5eDqNk63mLXsQ78n4RrubIrjtE0'
QINIU_BUCKET_NAME = 'clickz'
QINIU_HOST = 'http://image.12xiong.top/'
# from  day365_server.settings  import *
# from day365_server.settings import (QINIU_ACCESS_KEY,
#                                  QINIU_SECRET_KEY,
#                                  QINIU_BUCKET_NAME)

# assert QINIU_ACCESS_KEY and QINIU_SECRET_KEY and QINIU_BUCKET_NAME
import sys
import os
import logging
# logger
logger = logging.getLogger(__name__)

class QiNiu():
    def getToken(self,file_name):
        q = qiniu.Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
        # key = file_name
        key = file_name
        token = q.upload_token(QINIU_BUCKET_NAME,key = key ,policy = {"insertOnly": 0},)
        return token

    def delete(self,key):
        # try:
            #初始化Auth状态
        q = qiniu.Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
        #初始化BucketManager
        bucket = qiniu.BucketManager(q)
        #删除bucket_name 中的文件 key  #你要测试的空间， 并且这个key在你空间中存在
        ret, info = bucket.delete(QINIU_BUCKET_NAME, key)
        print(info)

if __name__ == "__main__":
    q = QiNiu()
    print q.getToken("123")