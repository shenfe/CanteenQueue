import scrapy


domain = 'http://www.zdic.net'


def req_list(i, callback):
    return scrapy.Request(
        url='http://www.zdic.net/z/zb/?n1=ty&n2=' + str(i),
        headers={
            'Accept': ['text/javascript', 'text/html', 'application/xml', 'text/xml', '*/*'],
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://www.zdic.net/z/zb/ty.htm' # 现代汉语通用字表
        }
    )


class ListSpider(scrapy.Spider):
    name = 'list'

    def start_requests(self):
        return map(lambda i: req_list(i, self.parse), range(5))

    def parse(self, response):
        for quote in response.css('a'):
            yield {
                'word': quote.xpath('text()').extract_first(),
                'link': domain + quote.xpath('@href').extract_first().replace('/js/', '/xs/')
            }
