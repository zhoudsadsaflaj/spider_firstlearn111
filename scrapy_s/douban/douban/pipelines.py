# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import csv


class DoubanPipeline:

    

    def process_item(self, item, spider):
       
        download_path=os.getcwd()+'/download/'#确定下载路径
        if not os.path.exists(download_path):#如果对应位置没有文件夹，就创建一个新的文件夹
            os.makedirs(download_path)
        
        msg_type=item.get('type')
        #保存基本信息
        # {#返回一个字典数据
        #             'type':'info',#这里确定字典的类型是info
        #             'img_src':img_src,
        #             'title':title,
        #             'rating_num':rating_num,
        #             'renew_num':renew_num,
            #         }
        if msg_type=='info':
            with open(download_path+'douban_top250.csv','a',encoding='utf-8') as f:
                #创建csv中的DictWriter对象，这样才能将数据写入csv文件格式里面
                f_csv=csv.DictWriter(f,['title','img_src','rating_num','renew_num'])
                item.pop('type')
                f_csv.writeheader()
                f_csv.writerow(item)
                print("-----info_sucess_store-----")
        
        #保存图片
        # {
        #     'type':'img',
        #     'img_name':img_name,
        #     'img':response.body
        # }
        elif msg_type=='img':
            img_dir = os.path.join(download_path, 'image')
            if not os.path.exists(img_dir):#如果对应位置没有文件夹，就创建一个新的文件夹
                os.makedirs(img_dir)
            img_path = os.path.join(img_dir, item.get('img_name'))
            with open(img_path,'wb') as f:
                f.write(item.get('img'))
                print("-----msg_success_store-----")


        return item
