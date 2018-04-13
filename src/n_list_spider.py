import scrapy
import json
import re


domain = 'http://www.zdic.net'


def read_pys():
    file = open('./src/data/list.json', 'rb')
    return json.load(file)


records = {}


def check_dup(w):
    if w in records:
        return True
    records[w] = True
    return False


class DictSpider(scrapy.Spider):
    name = 'n_dict'

    def start_requests(self):
        return map(lambda item: scrapy.Request(
            url='http://www.zdic.net/c/cipy/ci/sc/?z=' + item['word'],
            headers={
                'Accept': ['text/javascript', 'text/html', 'application/xml', 'text/xml', '*/*'],
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'http://www.zdic.net/c/cipy/ci/?z=' + item['word']
            }
        ), read_pys())

    def parse(self, response):
        arr = response.css('.zlist li a')
        for item in arr:
            w = item.xpath('text()').extract_first()
            if check_dup(w):
                continue
            yield {
                'word': w,
                'link': domain + item.xpath('@href').extract_first()
            }
