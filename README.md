# Chinesemess

Something really complicated about Chinese language...

## Spider

The spiders crawl data from [汉典网](http://www.zdic.net).

### Dependencies

* Python3

    ```bash
    $ pip install scrapy
    ```

    If the OS is Windows, it requires [pywin32](https://github.com/mhammond/pywin32) perhaps. Install it by `pip install pywin32`.

### Commands

```bash
$ scrapy runspider src/list_spider.py -o src/data/list.json -s FEED_EXPORT_ENCODING='utf-8' # Step1: fetch the list of Chinese characters
$ scrapy runspider src/dict_spider.py -o src/data/dict.json -s FEED_EXPORT_ENCODING='utf-8' # Step2: fetch the dictionary
$ scrapy runspider src/pinyin_list_spider.py -o src/data/pinyin_simple.json -s FEED_EXPORT_ENCODING='utf-8' # fetch simple pinyin list
$ scrapy runspider src/n_list_spider.py -o src/data/n_list.json -s FEED_EXPORT_ENCODING='utf-8' # fetch the list of Chinese words
```
