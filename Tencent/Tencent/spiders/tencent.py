# -*- coding: utf-8 -*-
import re

import scrapy

from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        item = []
        for each in response.xpath('//*[@class="even"]'):

            item = TencentItem()
            name = each.xpath('./td[1]/a/text()').extract()[0]
            detail_link = each.xpath('./td[1]/a/@href').extract()[0]
            job_info = each.xpath('./td[2]/text()').extract()[0]
            people_number = each.xpath('./td[3]/text()').extract()[0]
            work_city = each.xpath('./td[4]/text()').extract()[0]
            publish_date = each.xpath('./td[5]/text()').extract()[0]

            item['name'] = name.encode('utf-8')
            item['detail_link'] = detail_link.encode('utf-8')
            item['job_info'] = job_info.encode('utf-8')
            item['people_number'] = people_number.encode('utf-8')
            item['work_city'] = work_city.encode('utf-8')
            item['publish_date'] = work_city.encode('utf-8')

            # 翻页
            curpage = re.search('(\d+)', response.url).group(1)
            page = int(curpage) + 10
            url = re.sub('\d+', str(page), response.url)

            # 发送新的url请求加入待爬队列，并调用回调函数 self.parse
            yield scrapy.Request(url, callback=self.parse)

            # 将获取的数据交给pipeline
            yield item
