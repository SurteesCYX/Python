
import os
from scrapy.pipelines.files import FilesPipeline
from eastmoney import settings
from pymongo import MongoClient
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class EastmoneyPipeline(object):
    
    def __init__(self):
        #连接mongo数据库,并把数据存储
        client = MongoClient()
        db = client.指数
        self.books = db.sz300766
        
    def process_item(self, item, spider):
        print ('spider_name',spider.name)
        temp ={'views':item['views'],
               'comments':item['comments'],
               'day':item['day'],
               'time':item['time'],
               'title_content':item['title_content'],
               'inner_content':item['inner_content']
               }
        self.books.insert(temp)

        return item
