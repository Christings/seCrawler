import scrapy


class KeywordspiderItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    abstract = scrapy.Field()
