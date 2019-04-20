# -*- coding: utf-8 -*-
import scrapy
from sdspider.items import SdspiderItem


class SdSpider(scrapy.Spider):
    name = 'sd'
    allowed_domains = ['www.creditsd.gov.cn']
    url = 'http://www.creditsd.gov.cn/creditsearch.punishmentList.phtml?id=&keyword=&page='
    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        link_lists = response.xpath('//table[@class="table table-hover table-condensed tab-content"]//a/@href').extract()
        for link in link_lists :
            url = 'http://www.creditsd.gov.cn' + link
            yield scrapy.Request(url = url, callback= self.parse_item)

        if self.offset < 100:
            self.offset += 1
            yield scrapy.Request(url = 'http://www.creditsd.gov.cn/creditsearch.punishmentList.phtml?id=&keyword=&page=' + str(self.offset)
                                 ,callback= self.parse)

    def parse_item(self, response):
        links= response.xpath('//*[@id="table1"]/div[2]/table')
        for li in links :
            item = SdspiderItem()
            item["num"] = li.xpath("./tr[4]/td[1]/text()").extract()[0].encode("utf-8")
            item["name"] = li.xpath("./tr[1]/td[1]/text()").extract()[0].encode("utf-8")
            item["result"] = li.xpath("./tr[14]/td[1]/text()").extract()[0].encode("utf-8")
            item["reason"] = li.xpath("./tr[6]/td[1]/text()").extract()[0].encode("utf-8")
            item["date"] = li.xpath("./tr[15]/td[1]/text()").extract()[0].encode("utf-8")
            item["unit"] = li.xpath("./tr[2]/td[1]/text()").extract()[0].encode("utf-8")
            yield item
