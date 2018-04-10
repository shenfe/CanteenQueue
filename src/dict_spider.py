import scrapy
import json
import re


def read_urls():
    file = open('./src/data/list.json', 'rb')
    arr = json.load(file)
    return list(map(lambda item: item['link'], arr))


def find_cx(ps, i):
    for j in range(i, len(ps)):
        if check_cx(ps, j):
            break
        p = ps[j].xpath('text()').extract_first()
        if not p or not (p.startswith('<') or p.startswith('〈')):
            continue
        p = re.search(r'(<|〈)(.*?)(>|〉)', p)
        if p is None:
            continue
        p = p.group(2)
        if p is not None:
            return p


def find_py(ps, i):
    p = None
    for j in range(i, len(ps)):
        p = ps[j].css('span.dicpy').xpath('text()').extract_first()
        if p is not None:
            break
    return p


def check_cx(ps, i):
    p = ps[i].extract()
    return p.find('◎') != -1


class DictSpider(scrapy.Spider):
    name = 'dict'
    start_urls = read_urls()

    def parse(self, response):
        char = response.css('div#ziip::text').extract_first()
        if char is None:
            return
        char = re.search(r'“(.*?)”.*', char)
        if char is None:
            return
        char = char.group(1)

        ps = response.css('div.tab-page p')
        content = []
        for i in range(len(ps)):
            if not check_cx(ps, i):
                continue
            # word = re.search(r'<strong>(.*?)</strong>', p).group(1)
            type_ = find_cx(ps, i + 1)
            pinyin = find_py(ps, i)
            content.append({
                'pronounce': pinyin,
                'type': type_
            })
        yield {
            'word': char,
            'records': content
        }
