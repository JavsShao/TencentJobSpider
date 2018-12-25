# -*- coding: utf-8 -*-
import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['www.tencent.com']
    start_urls = ['http://www.tencent.com/']

    def parse(self, response):
        pass
