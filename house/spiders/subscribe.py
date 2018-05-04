# -*- coding: utf-8 -*-
import scrapy
from house.items import HouseItem
import re


class SubscribeSpider(scrapy.Spider):
    name = 'subscribe'
    allowed_domains = ['https://hz.fang.anjuke.com/']
    start_urls = [
        # 'https://hz.fang.anjuke.com/loupan/yuhang_1921/s6_w1/',

        # 'https://hz.fang.anjuke.com/loupan/yuhang_1923/s6_w1/',

        # 'https://hz.fang.anjuke.com/loupan/yuhang_1924/s6_w1/',

        'https://hz.fang.anjuke.com/loupan/all/s6_w1/',
    ] + ['https://hz.fang.anjuke.com/loupan/all/p{0}_s6_w1/'.format(i) for i in range(2, 10)]

    def parse(self, response):
        for item in response.css('.key-list .item-mod'):
            href = item.css('.lp-name::attr(href)').extract_first()
            project_name = item.css('.items-name::text').extract_first()

            huxing = item.css('.huxing>span::text').extract()

            size = huxing[-1]
            huxing = huxing[:-1]

            status_tags = item.css('.status-icon::text').extract()
            status = status_tags[0]
            htype = status_tags[1]

            yield HouseItem(
                project_name=project_name,
                href=href, huxing=huxing,
                size=size, htype=htype,
                status=status
            )
        pass
