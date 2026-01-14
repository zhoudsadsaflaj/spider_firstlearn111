import os
import time
import requests

url='https://gips1.baidu.com/it/u=3874647369,3220417986&fm=3028&app=3028&f=JPEG&fmt=auto?w=720&h=1280'

start_time=time.time()

response=requests.get(url=url)

stop_time=time.time()

#print(f'耗费时间{stop_time-start_time}')

#print('img--->',response.content)

file_path='./download/image/'

if not os.path.exists(file_path):
    os.makedirs(file_path)

with open(os.path.join(file_path,'1.jpg'),'wb') as f:
    f.write(response.content)