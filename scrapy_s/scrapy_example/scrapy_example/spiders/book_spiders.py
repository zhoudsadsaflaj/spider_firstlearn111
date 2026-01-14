import scrapy
from scrapy import cmdline
from ..items import BookItem
from scrapy.linkextractors import LinkExtractor

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls=["http://books.toscrape.com/"]

    def parse(self,response):
        for book in response.css("article.product_pod"):

            #1
            '''name=book.xpath('./h3/a/@title').get()
            price=book.css('p.price_color::text').get()'''
            
            bookn=BookItem()
            bookn['name']=book.xpath('./h3/a/@title').get()
            bookn['price']=book.css('p.price_color::text').get()
            #1
            """yield{
                'name':name,
                'price':price
            }"""
            yield bookn
            
            #获取下一页1
            '''next_url=response.css('ul.pager li.next a::attr(href)').get()

            if next_url:
                next_url=response.urljoin(next_url)
                yield scrapy.Request(next_url,callback=self.parse)'''
            
            #获取下一页1
            le=LinkExtractor(restrict_css='ul.pager li.next')
            links=le.extract_links(response)
            if links:
                next_url=links[0].url
                yield scrapy.Request(next_url,callback=self.parse)


if __name__=='__main__':
    cmdline.execute('scrapy crawl books -o books.csv'.split())