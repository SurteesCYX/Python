# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EastmoneyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    views = scrapy.Field()
    comments = scrapy.Field()
    day = scrapy.Field()
    time = scrapy.Field()
    title_content = scrapy.Field()
    inner_content = scrapy.Field()
    pass
