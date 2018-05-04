# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    href = scrapy.Field()
    project_name = scrapy.Field()
    huxing = scrapy.Field()
    size = scrapy.Field()
    status = scrapy.Field()
    htype = scrapy.Field()