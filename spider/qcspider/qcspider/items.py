# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# class BrandItem(scrapy.Item):
#     id = scrapy.Field()
#     name = scrapy.Field()
#     url = scrapy.Field()
#     pic = scrapy.Field()

class SeriesItem(scrapy.Item):
    id = scrapy.Field()
    brand_id = scrapy.Field()
    manu_name = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()


