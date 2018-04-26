#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Lilly'

import scrapy
from scrapy.spiders import Spider
from seCrawler.common.searResultPages import searResultPages
from seCrawler.common.searchEngines import SearchEngineResultSelectors

from scrapy.selector import Selector
from seCrawler.items import KeywordspiderItem


class keywordSpider(Spider):
    name = 'keywordSpider'
    allowed_domains = ['bing.com', 'google.com', 'baidu.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None

    def __init__(self, keyword, se='bing', pages=50, *args, **kwargs):
        super(keywordSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        pageUrls = searResultPages(keyword, se, int(pages))
        for url in pageUrls:
            print("url:", url)
            self.start_urls.append(url)

    # def parse(self, response):
    #     for url in Selector(response).xpath(self.selector).extract():
    #         yield scrapy.Request(url, self.parse_text)
    #         # yield {'url': url}
    #
    def parse_text(self, response):
        text = response.body.decode('utf-8', 'ignore')  # 把结果解析为中文的格式来显示
        with open(r'files/' + response.meta['title'] + '.txt', 'w', encoding='utf-8') as file:
            file.write(text)
            file.close()
            # pattarn = re.compile(r'<[^>]+>', re.S)
            # content = pattarn.sub('', text)
            # text = response.body
            #
            # with open(r'files/' + response.meta['title'] + '.txt', 'w', encoding='utf-8') as file:
            #     file.write(str(text))
            #     file.close()
            #     # with open(r'files/' + response.meta['title'] + '.txt', 'wb') as file:
            #     #     file.write(text.encode(encoding='gb18030', errors='ignore'))
            #     #     file.close()

    def parse(self, response):
        item = KeywordspiderItem()
        # a 用来解决IndexError: list index out of range越界的问题
        a = []
        for i in range(1, 1001):
            a.append(['%d' % i])
        if self.searchEngine == 'baidu':
            for each in Selector(response).xpath(self.selector):
                if each.xpath('./@id').extract() in a:
                    item['title'] = (''.join(each.xpath('./h3/a//text()').extract())).replace('|', '').replace('?',
                                                                                                               '').strip()
                    item['url'] = each.xpath('./h3/a/@href').extract()[0]
                    item['time'] = (''.join(each.xpath('./div[@class="c-abstract"]/span/text()').extract())).replace(
                        '\xa0-', '').strip()
                    item['abstract'] = (''.join(each.xpath('./div[@class="c-abstract"]//text()').extract())).replace(
                        ',',
                        '').strip()
                    url = item['url']
                    yield scrapy.Request(url, meta={'title': item['title']}, callback=self.parse_text)
                yield item
        elif self.searchEngine == 'google':
            for each in Selector(response).xpath(self.selector):
                item['title'] = (''.join(each.xpath('.//h3/a//text()').extract()).strip())
                # print(item['title'])
                item['url'] = each.xpath('.//h3/a/@href').extract()[0]
                # print(item['url'])
                item['abstract'] = (''.join(each.xpath('.//div[@class="s"]/div/span//text()').extract()))
                # print(item['abstract'])
                yield item
        elif self.searchEngine == 'bing':
            for each in Selector(response).xpath(self.selector):
                # 解决IndexError: list index out of range的bug，因为each.xpath('.//h2/a/@href').extract()[0]提取不到
                if len(each.xpath('.//h2/a/@href').extract()):
                    item['title'] = (''.join(each.xpath('.//h2/a//text()').extract()).strip())
                    print(item['title'])
                    item['url'] = each.xpath('.//h2/a/@href').extract()[0]
                    print(item['url'])
                    item['abstract'] = (''.join(each.xpath('./div[@class="b_caption"]/p//text()').extract()))
                    print(item['abstract'])
                yield item
