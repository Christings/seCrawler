from scrapy import cmdline

cmdline.execute("scrapy crawl keywordSpider -a keyword=农业企业走出去问题 -a se=baidu -a pages=15".split())