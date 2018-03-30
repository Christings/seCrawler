__author__ = 'Lilly'
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

    def parse(self, response):
        item = KeywordspiderItem()
        # a 用来解决IndexError: list index out of range越界的问题
        a = []
        for i in range(1, 101):
            a.append(['%d' % i])
        if self.searchEngine == 'baidu':
            for each in Selector(response).xpath(self.selector):
                if each.xpath('./@id').extract() in a:
                    item['title'] = (''.join(each.xpath('./h3/a//text()').extract()).strip())
                    item['url'] = each.xpath('./h3/a/@href').extract()[0]
                    item['abstract'] = (''.join(each.xpath('./div[@class="c-abstract"]//text()').extract())).replace(
                        ',',
                        '').strip()
                    # for url in Selector(response).xpath(self.selector).extract():
                    #     # yield {'url':url}  不使用item，直接存储到txt文件中。
                    #     item['url'] = url
                    #     yield item
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
        pass
