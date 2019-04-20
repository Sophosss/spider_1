# -*- coding: utf-8 -*-
import scrapy
from qcspider.items import SeriesItem

class SeriesSpider(scrapy.Spider):
    name = 'series'
    allowed_domains = 'autohome.com.cn'
    start_urls = ['http://www.autohome.com.cn/grade/carhtml/%s.html' % chr(ord('A') + i) for i in range(2)]

    def parse(self, response):
        for brandPart in response.xpath('body/dl'):
            series = SeriesItem()
            brand_id = brandPart.xpath('@id')[0].extract()
            manu_name = brandPart.xpath('dd/div/a/text()')[0].extract()
            seriesParts = brandPart.xpath('dd/ul/li')
            for seriesPart in seriesParts:
                try:
                    series['brand_id'] = brand_id
                    series['manu_name'] = manu_name
                    series['id'] = seriesPart.xpath('@id')[0].extract()
                    series['name'] = seriesPart.xpath('h4/a/text()')[0].extract()
                    series['url'] = seriesPart.xpath('h4/a/@href')[0].extract()
                    yield series
                except:
                    pass
