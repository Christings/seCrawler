from scrapy import cmdline
cmdline.execute("scrapy crawl keywordSpider -a keyword=张韶涵 -a se=bing -a pages=1".split())