import scrapy
import json


def read_urls():
    file = open("./src/data/list.json", "rb")
    arr = json.load(file)
    return list(map(lambda item: item["link"], arr))


class DictSpider(scrapy.Spider):
    name = 'dict'
    start_urls = read_urls()

    def parse(self, response):
        for page in response.css('div.tab-page'):
            yield {
                'char': '--'
            }
