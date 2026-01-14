import scrapy


class ProxyTextSpider(scrapy.Spider):
    name = "proxy_text"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        print('-----回调函数-----',response)
