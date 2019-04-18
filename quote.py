# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from eastmoney.items import EastmoneyItem
import requests

class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['guba.eastmoney']
    start_urls = ['http://guba.eastmoney.com/list,300766,f.html']

    def parse(self, response):
        selector = Selector(response)
        tiezi= selector.xpath("//div[@class='articleh normal_post']" or "//div[@class='articleh normal_post odd']")
        for i in range(len(tiezi)):
            item = EastmoneyItem()
            box = tiezi[i]
            try:               
                item['views'] = int(box.xpath(".//span[@class='l1']/text()").extract()[0]) #帖子浏览量
                item['comments'] = int(box.xpath(".//span[@class='l2']/text()").extract()[0])#帖子点击率
                item['day'] = (box.xpath(".//span[@class='l5']/text()").extract()[0]).split(" ")[0]#发帖日期
                item['time'] = (box.xpath(".//span[@class='l5']/text()").extract()[0]).split(" ")[1]#发帖时间
                item['title_content'] =  str(box.xpath(".//span[@class='l3']/a/text()").extract())#帖子标题
                item['inner_content']=Selector(requests.get('http://guba.eastmoney.com'+ box.xpath(".//span[@class='l3']/a/@href").extract()[0])).xpath("//div[@class='xeditor_content']/p/text()").extract()#帖子内容
                yield item
            except Exception as e:
                print ('excepiton',e)