import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import MatplotlibExamplesItem


class MatplotlibSpider(scrapy.Spider):
    name = "matplotlib"
    allowed_domains = ["matplotlib.org"]
    start_urls = ['http://matplotlib.org/examples/index.html']

    def parse(self, response):
        le=LinkExtractor(restrict_css='div.toctree-wrapper.compound',deny='/index.html$')

        links=le.extract_links(response)
        for link in links:
            yield scrapy.Request(link.url,callback=self.parse_file)

        
    def parse_file(self,response):
        href=response.css("div.section a.reference.external::attr(href)").get()
        url=response.urljoin(href)
        matplotlib=MatplotlibExamplesItem()
        matplotlib['file_urls']=[url]

        yield matplotlib

