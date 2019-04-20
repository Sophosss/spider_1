# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import json

class JsspiderPipeline(object):
    def __init__(self):
        """
        打开文件，获取文件句柄
        """
        self.f = open('jsfda.json', 'wb')

    def process_item(self, item, spider):
        """
        写入文件
        :param item: 存储数据对象
        :param spider: 爬虫对象
        :return:
        """
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.f.write(content.encode('utf8'))
        return item

    def close_spider(self, spider):
        """
        爬虫结束自动调用的函数，用于关闭文件句柄
        :param spider: 爬虫对象
        :return:
        """
        self.f.close()
