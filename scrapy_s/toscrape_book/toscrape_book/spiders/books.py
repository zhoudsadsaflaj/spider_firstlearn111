import scrapy
from ..items import ToscrapeBookItem
from scrapy.linkextractors import LinkExtractor


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]


    # 1. 初始化一个页面计数器
    page_count = 1
    # 2. 设置最大页面数
    max_pages = 2

    def parse(self, response):
        le=LinkExtractor(restrict_css='article.product_pod h3')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url,callback=self.parse_book)
        
        le=LinkExtractor(restrict_css='ul.pager li.next')
        links=le.extract_links(response)
        if links:
            if self.page_count >= self.max_pages:
                self.log(f'已爬取 {self.page_count} 页，达到最大页数限制，停止爬取新页面。')
                return # 停止生成下一页的请求
            self.page_count += 1 # 4. 页面计数器加一
            yield scrapy.Request(links[0].url,callback=self.parse)

    def parse_book(self,response):
        book=ToscrapeBookItem()

        sel=response.css('div.product_main')
        book['name']=sel.css('h1::text').get()
        book['price']=sel.css('p.price_color::text').get()
        book['review_rating']=sel.css('p.star-rating::attr(class)').re_first('star-rating([A-Za-z]+)')

        sel=response.css('table.table-striped')
        book['upc']=sel.css('tr:first_child td::text').get()
        book['stock']=sel.xpath('.//tr[last()-1]/td/text()').re_first('\((\d+) available\)')
        book['review_num']=sel.xpath('.//tr[last()]/td/text()').get()

        yield book

