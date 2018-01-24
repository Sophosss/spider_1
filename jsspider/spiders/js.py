# -*- coding: utf-8 -*-
import scrapy
from jsspider.items import JsspiderItem

class JsSpider(scrapy.Spider):
    name = 'js'
    allowed_domains = ['www.jsfda.gov.cn']
    start_urls = ['http://www.jsfda.gov.cn/fwdt/datasearch/sgs/sgsxzcf/',
                  'http://www.jsfda.gov.cn/fwdt/datasearch/sgs/sgsxzcf/index_1.html']

    def parse(self, response):
        link_lists = response.xpath ("//*[@id='result']//a/@href").extract()
        for link in link_lists :
            url = 'http://www.jsfda.gov.cn/fwdt/datasearch/sgs/sgsxzcf/'+ link.strip('./')
            yield scrapy.Request(url=url , callback=self.parse_item)

    def parse_item(self, response):
        links = response.xpath ("//table")
        for li in links :
            item = JsspiderItem()
            item["num"] = li.xpath("./tr[1]/td[2]/text()").extract()[0].encode("utf-8")
            item["name"] = li.xpath("./tr[13]/td[2]/text()").extract()[0].encode("utf-8")
            item["result"] = li.xpath("./tr[14]/td[2]/text()").extract()[0].encode("utf-8")
            item["date"] = li.xpath("./tr[15]/td[2]/text()").extract()[0].encode("utf-8")
            item["unit"] = li.xpath("./tr[16]/td[2]/text()").extract()[0].encode("utf-8")
            yield item


