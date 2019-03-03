# -*- coding: utf-8 -*-
import jieba

comment_list = ['\xcd\xdb\xc4\xcf\xc4\xfe\xb5\xc4\xd0\xa1\xbd\xe3\xbd\xe3', '\xc4\xd4\xb2\xb9\xd7\xd4\xbc\xba\xd7\xf8\xd4\xda\xc0\xef\xc3\xe6\xc5\xc4\xd5\xd5 \xb9\xfe\xb9\xfe\xb9\xfe', '\xc8\xcb\xc3\xc0\xb5\xea\xc3\xc0', '\xc0\xef\xc3\xe6\xd3\xd0\xb2\xde\xcb\xf9\xc2\xf0', '\xcf\xb2\xbb\xb6\xb4\xa9\xb4\xee \xba\xc3\xd3\xd0\xc6\xf8\xd6\xca', '\xc6\xf8\xd6\xca\xb5\xc4\xc4\xe3', '\xb2\xbb\xd6\xaa\xb5\xc0\xc9\xcf\xba\xa3\xd3\xd0\xc3\xbb\xd3\xd0\xd1\xbd[\xba\xc8\xc4\xcc\xb2\xe8R][\xba\xc8\xc4\xcc\xb2\xe8R][\xba\xc8\xc4\xcc\xb2\xe8R]', '\xc0\xb4\xb1\xed\xd1\xef\xd5\xe2\xbc\xfe\xcd\xe2\xcc\xd7\xa1\xab', '\xc3\xc0\xc0\xf6\xc3\xc0\xc0\xf6\xa3\xa1', 'LV\xb5\xc4\xb0\xfc\xb0\xfc\xba\xc3\xbf\xb4\xd1\xbd\xa3\xa1\xa3\xa1', '\xbb\xc6\xca\xab\xca\xab \xd4\xd9\xb4\xce\xce\xca\xba\xc3', '\xd3\xd6\xca\xc7\xd6\xaa\xd0\xd4\xb5\xc4\xd2\xbb\xcc\xec\xa1\xab', '\xb0\xfc\xb0\xfc\xc3\xc0\xbf\xde\xc1\xcb', '\xcf\xb2\xbb\xb6\xc4\xe3', '\xb0\xfc\xb0\xfc\xd5\xe6\xba\xc3\xbf\xb4\xb0\xa1', '\xcf\xb2\xbb\xb6ins\xb7\xe7', '\xbb\xb7\xbe\xb3\xd5\xe6\xba\xc3\xa3\xac\xcf\xeb\xc8\xa5\xc5\xc4\xd5\xd5[\xd0\xb1\xd1\xdbR]', '\xbf\xb4\xc0\xb4\xd2\xaa\xc0\xb4\xc4\xcf\xc4\xfe\xb4\xf2\xbf\xa8', '\xbb\xb7\xbe\xb3\xb2\xbb\xb4\xed\xc4\xd8', '\xb7\xa2\xd5\xb9\xba\xc3\xba\xc3\xbf\xb4\xa3\xa1', '\xcd\xdb\xc8\xfb \xc4\xcf\xc4\xfe\xba\xc3\xb6\xe0\xb2\xbb\xb4\xed\xb5\xc4\xb5\xea\xb0\xbe', '\xcf\xb2\xbb\xb6\xd5\xe2\xbc\xfe\xb4\xf3\xd2\xc2', '\xc3\xc0\xc0\xf6\xd2\xbb\xc8\xe7\xbc\xc8\xcd\xf9\xb5\xc4\xc3\xc0', '\xb4\xf3\xb7\xbd\xc6\xaf\xc1\xc1\xb5\xc4\xc3\xc0\xc0\xf6^^', '\xcf\xb2\xbb\xb6\xcd\xe2\xcc\xd7\xb0\xa1', '\xc7\xf3\xcd\xe2\xcc\xd7', '\xd5\xe2\xcc\xf5\xbf\xe3\xd7\xd3\xba\xf0\xba\xf0\xbf\xb4', '\xd7\xb0\xd0\xde\xd5\xe6\xc3\xc0\xa1\xab', '\xc8\xcb\xb2\xbb\xb6\xe0\xda\xc0', '\xba\xc3\xb0\xf4', '\xb4\xf3\xd1\xdb\xbe\xa6\xbf\xa7\xb7\xc8', '\xb2\xb6\xd7\xbd\xb5\xbd\xd2\xbb\xb8\xf6\xc4\xcf\xc4\xfe\xc3\xc0\xc5\xae[\xc9\xab\xc9\xabR]', '\xba\xc3\xcf\xeb\xc8\xa5', '\xba\xc3\xcf\xeb\xc8\xa5', '\xd3\xc5\xd1\xc5\xc5\xae\xc9\xf1', '\xd5\xe2\xbc\xd2\xb5\xea\xcc\xab\xba\xc3\xc5\xc4\xc1\xcb', '\xba\xc3\xc3\xc0', '\xbf\xb4\xd7\xc5\xba\xc3\xca\xe6\xb7\xfe', '[\xba\xc8\xc4\xcc\xb2\xe8R]\xbb\xb7\xbe\xb3\xba\xc3\xb0\xf4\xa1\xab', '\xc5\xa3\xd7\xd0\xbf\xe3\xba\xc3\xbf\xb4\xda\xc0\xa3\xa1\xa3\xa1', '\xcf\xb2\xbb\xb6\xb8\xf1\xd7\xd3\xcd\xe2\xcc\xd7\xa1\xab', '\xd5\xe2\xb8\xf6\xb0\xfc\xba\xc3\xba\xc3\xbf\xb4\xa3\xa1', '\xb3\xac\xcf\xb2\xbb\xb6\xcd\xbc1[\xd4\xdeR][\xd4\xdeR]', '\xd5\xe2\xd6\xd6\xb5\xf7\xb5\xf7\xb3\xac\xca\xe6\xb7\xfe\xa3\xa1', '\xb0\xfc\xb0\xfc\xba\xc3\xca\xca\xba\xcf\xc4\xe3', '\xcf\xb2\xbb\xb6\xd5\xe2\xb8\xf6\xb5\xf7\xb5\xf7', '\xc3\xc0\xc3\xc0\xdf\xd5', '\xba\xc3\xcf\xb2\xbb\xb6', '\xb7\xe7\xb8\xf1\xba\xc3\xcf\xb2\xbb\xb6', '\xb0\xb2\xb0\xb2\xbe\xb2\xbe\xb2\xb5\xc4 \xd5\xe6\xba\xc3', '\xd5\xe2\xbc\xd2\xba\xc3\xbf\xb4', '\xd5\xe2\xbc\xd2\xb5\xea\xcc\xab\xd1\xf3\xc6\xf8\xc1\xcb', '\xba\xc3\xba\xc3\xbf\xb4\xd1\xbd']



# seg_list = jieba.cut_for_search(comment_list[0]), cut_all=False)  # 搜索引擎模式
# key_list = []
counts = {}

for c in comment_list:
    words = jieba.lcut(c, cut_all=False)
    # print seg_list[0]
    for word in words:
        counts[word] = counts.get(word,0) + 1

    # key = (", ".join(words))
    # key_list.append(key)
# print key_list
# for k in key_list:
#     print k
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(0,len(items)):
    word, count = items[i]
    print word,count
    # print ("{0:<10}{1:>5}".format(word, count))