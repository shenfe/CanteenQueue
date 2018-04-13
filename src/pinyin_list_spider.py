import scrapy


def req_list(i, callback):
    return scrapy.Request(
        url='http://www.zdic.net/c/cipy/'
    )


class Spider(scrapy.Spider):
    name = 'pinyin_list'
    start_urls = [
        'http://www.zdic.net/c/cipy/'
    ]

    def parse(self, response):
        for quote in response.css('a'):
            yield {
                'word': quote.xpath('text()').extract_first(),
                'link': domain + quote.xpath('@href').extract_first().replace('/js/', '/xs/')
            }