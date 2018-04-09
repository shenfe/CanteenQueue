# chinesemess

Something about Chinese language.

## spider

The spider crawls Chinese characters with basic explanations from [zdic.net](http://www.zdic.net).

### dependencies

`scrapy`

### commands

```bash
$ scrapy runspider src/list_spider.py -o src/data/list.json -s FEED_EXPORT_ENCODING='utf-8'
$ scrapy runspider src/dict_spider.py -o src/data/dict.json -s FEED_EXPORT_ENCODING='utf-8'
```
