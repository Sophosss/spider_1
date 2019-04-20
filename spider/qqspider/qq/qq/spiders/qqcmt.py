# -*- coding: utf-8 -*-
import scrapy
import json
from qq.items import QqItem


class QqcmtSpider(scrapy.Spider):
    name = 'qqcmt'
    allowed_domains = ['user.qzone.qq.com']
    offset = 0
    url = "https://user.qzone.qq.com/proxy/domain/m.qzone.qq.com/cgi-bin/new/get_msgb?uin=1477261167&hostUin=1477261167&start="
    s = '&s=0.7150095267777417&format=jsonp&num=10&inCharset=utf-8&outCharset=utf-8&g_tk=679287437&qzonetoken=4b78e2790bdcb05af85aac82808557e7911767bf58eeb2560bf9f88155b4b839b9cde7d1f8a73f17ee&g_tk=679287437'
    start_urls = [url + str(offset) + s]
    def parse(self, response):
        data = json.loads(response.text)["commentList"]

        for each in data:
            item = QqItem()
            item["name"] = each["nickname"]
            # item["time"] = each["pubtime"]
            # item["content"] = each["ubbContent"]

            yield item


        if self.offset < 70:
            self.offset += 10
            yield scrapy.Request(self.url + str(self.offset) + self.s , callback=self.parse, dont_filter=True)
