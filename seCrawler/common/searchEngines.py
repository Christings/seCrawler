__author__ = 'Lilly'

SearchEngines = {
    'google': 'https://www.google.com/search?q={0}&start={1}',
    'bing': 'http://www.bing.com/search?q={0}&first={1}',
    'baidu': 'http://www.baidu.com/s?wd={0}&pn={1}'
}


# SearchEngineResultSelectors= {
#     'google': '//h3/a/@href',
#     'bing':'//h2/a/@href',
#     'baidu':'//h3/a/@href',
# }
SearchEngineResultSelectors= {
    'google': '//div[@class="srg"]/div',
    'bing':'//div[@id="b_content"]/ol[@id="b_results"]/li',
    'baidu':'//div[@id="content_left"]/div',
}
SearchEngineTitleSelectors= {
    'google': '//h3/a//text()',
    'bing':'//h2/a//text()',
    'baidu':'//h3/a//text()',
}
SearchEngineTimeSelectors= {
    'google': '',
    'bing':'',
    'baidu':'//div[@id="content_left"]/div[@class="c-abstract"]/span/text()',
}
SearchEngineAbstractSelectors= {
    'google': '//h3/a/@href',
    'bing':'//h2/a/@href',
    'baidu':'//div[@id="content_left"]/div/div[@class="c-abstract"]//text()',
}
