# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import os

class QqPipeline(object):

    def __init__(self):
        self.file = open("cmt.json", "w")

    def process_item(self, item, spider):
            name = "[\n" + json.dumps(dict(item), ensure_ascii=False, encoding="utf-8")

            self.file.write(name)

            return item

    def close_spider(self, spider):
        self.file.write("\n]")
        self.file.close()
