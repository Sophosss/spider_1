# -*- coding: utf-8 -*-
import scrapy
from jsSpider.items import JsspiderItem

class JsfdaSpider(scrapy.Spider):
    name = "jsfda"
    allowed_domains = ["www.jsfda.gov.cn"]
    url = 'http://www.jsfda.gov.cn/fwdt/datasearch/sgs/sgsxzcf/'
    start_urls = [
        'http://www.jsfda.gov.cn/fwdt/datasearch/sgs/sgsxzcf/',
        "http://www.jsfda.gov.cn/fwdt/datasearch/sgs/sgsxzcf/index_1.html"
    ]
    def parse(self, response):
        """
        解析scrapy框架自动爬取start_urls的response，并在页面匹配链接发送请求
        :param response: 响应对象
        :return:
        """
        links = response.xpath("//table//a/@href").extract()
        for link in links:
            if link.startswith('./'):
                link = self.url + link.strip('./')
                yield scrapy.Request(url=link, callback=self.parse_item)

    def parse_item(self, response):
        """
        解析新请求得到的response，用xpath提取想要的数据
        :param response: 响应对象
        :return:
        """
        for each in response.xpath("//table"):
            # 实例化存储对象
            item = JsspiderItem()
            item["number"] = each.xpath("./tr[1]/td[2]/text()").extract_first()
            item["result"] = each.xpath("./tr[14]/td[2]/text()").extract_first()
            item["unit"] = each.xpath("./tr[16]/td[2]/text()").extract_first()
            yield item


