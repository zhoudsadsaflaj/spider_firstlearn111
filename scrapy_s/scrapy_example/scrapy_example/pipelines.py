# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyExamplePipeline:
    def process_item(self, item, spider):
        return item


'''注意这里配置之后要将setting中的设置改一下'''
#这里是实现将￡变成￥
class PriceConverterPipeline(object):
    exchange_rate=8.5309

    def process_item(self,item,spider):
        price=float(item['price'][1:])*self.exchange_rate
        item['price']='￥%.2f'%price

        return item
    

#这里是进行去重操作
from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):
    def __init__(self):
        self.book_set=set()
    
    def process_item(self,item,spider):
        name=item['name']
        if name in self.book_set:
            raise DropItem(f"Duplicates book found{item}")
        
        self.book_set.add(name)

        return item
    
