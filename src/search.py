#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.index import create_in
from whoosh.index import open_dir
from jieba.analyse import ChineseAnalyzer
# from pyltp import Segmentor
analyzer = ChineseAnalyzer()
import os.path
# import pyltp
filename_list=[]
ID_list = []

schema = Schema(title=TEXT, content=TEXT)

schema = Schema(title=TEXT(stored=True, analyzer=analyzer), content=TEXT(stored=True, analyzer=analyzer),
                 ID=ID(stored=True),tags=KEYWORD, icon=STORED, )


# 遍历文件夹
# path_generator = os.walk("../blog_engine")
# for path,d,filelist in path_generator:
#     for filename in d:

ix = open_dir("../blog_engine")

try:
    result_add = []
    result_str = []
    key_add = []
    ID_add = []
    dict_pos_word = {}
    searcher = ix.searcher()

    '''
    :parameter
    content : 表示在文章里面搜索
    title : 表示在标题里面搜索
    search_str : 输入一个关键字
    '''
    search_str = u"科技"
    results = searcher.find("content",search_str)
    # print len(results)

    for hit in results:
        if hit.score > 0:
            if len(ID_add) <= 20:
                # 返回文章的ID位置
                print search_str
                ID_add.append(hit['ID'])
                print hit['ID']
                print hit.score
                print "-" * 50
                hit['ID'].encode('utf-8')

finally:
    searcher.close()