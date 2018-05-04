# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from subscribe import subscribe
import time

class HousePipeline(object):
    def process_item(self, item, spider):
        print(item['status'])
        if  item['status'] != '售罄':
            time.sleep(1)
            item_id = item['href'].split('/')[-1].split('.')[0]
            subscribe(item_id)
            return item
