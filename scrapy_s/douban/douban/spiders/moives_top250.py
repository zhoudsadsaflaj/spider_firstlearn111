import scrapy


class MoivesTop250Spider(scrapy.Spider):
    name = "moives_top250"
    allowed_domains = ["douban.com",'doubanio.com']
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        li_links=response.xpath("//ol[@class='grid_view']/li")

        for link in li_links:
            img_src=link.xpath(".//a/img/@src").get()
            title=link.xpath(".//span[@class='title']/text()").get()
            rating_num=link.xpath(".//span[@class='rating_num']/text()").get()
            renew_num=link.xpath(".//span[4]/text()").re_first(r'(\d+)人')

            print('----->',img_src,title,rating_num,renew_num)

            #保存的是链接和基本数据
            yield {#返回一个字典数据
                
                'type':'info',#这里确定字典的类型是info
                'img_src':img_src,
                'title':title,
                'rating_num':rating_num,
                'renew_num':renew_num,
            }



            #保存图片，从链接中保存图片

            yield scrapy.Request(url=img_src,callback=self.parse_img,cb_kwargs={'img_name':title})

        #下一页的
        le=response.xpath("//div[@class='paginator']/span[@class='next']/a/@href").get()
        print('-----下一页链接-----',le)
        yield scrapy.Request(url='https://movie.douban.com/top250'+le,callback=self.parse)

    #处理图片的回调函数
    def parse_img(self,response,img_name):
        print("-----处理图片的回调函数正在执行-----")

        yield{
            'type':'img',
            'img_name':img_name+'.jpg',
            'img':response.body
        }