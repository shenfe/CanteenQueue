import scrapy


class Spider(scrapy.Spider):
    name = 'pinyin_list'
    start_urls = [
        'http://www.zdic.net/c/cipy/'
    ]

    def parse(self, response):
        for item in response.css('div.pyul dl'):
            yield {
                'pinyin': item.css('dt a::text').extract_first(),
                'word': item.css('dd a::text').extract_first()
            }
