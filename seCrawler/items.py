import scrapy


class KeywordspiderItem(scrapy.Item):
    url = scrapy.Field()            # url
    title = scrapy.Field()          # 标题
    time = scrapy.Field()           # 发文时间
    company = scrapy.Field()        # 发文单位
    abstract = scrapy.Field()       # 摘要
    text = scrapy.Field()           # 全文
