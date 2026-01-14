import scrapy
import json
from ..items import ImagesExampleItem

class ImagesSpider(scrapy.Spider):
    base_url='https://image.so.com/zjl?sn=%s&ch=art'
    start_index=0
    MAX_DOWNLOAD_NUM=70
    name = "images"
    #这里域名设置太严格，在爬取的过程中跳转不出去
    #allowed_domains = ["image.so.com"]
    start_urls = [base_url %0]

    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))


        item=ImagesExampleItem()
        item["image_urls"]=[info['qhimg_url'] for info in infos["list"]]
        yield item
        
        """yield {
            'image_urls':[info['qhimg_url'] for info in infos["list"]]
        }"""
        
        self.start_index+=infos["count"]
        if infos["count"]>0 and self.start_index<self.MAX_DOWNLOAD_NUM:
            yield scrapy.Request(self.base_url %self.start_index)
    
    

