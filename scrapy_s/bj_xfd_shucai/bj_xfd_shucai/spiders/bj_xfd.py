import scrapy


class BjXfdSpider(scrapy.Spider):
    name = "bj_xfd"
    allowed_domains = ["xinfadi.com"]
    start_urls = ["http://www.xinfadi.com.cn/priceDetail.html"]

    def parse(self, response):
        pass
