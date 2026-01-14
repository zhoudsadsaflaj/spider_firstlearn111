import requests

import time


vedio_url='https://v26-hl-cold.douyinvod.com/2ccbad24bddaf5ffc592be23b180db83/6960804a/video/tos/cn/tos-cn-ve-15/o8o6gMXrQ9Ex6VNkBGMARs5b7eRAICfBrBQO8f/?a=1128&ch=0&cr=0&dr=0&lr=aweme_search_suffix&cd=0%7C0%7C1%7C0&cv=1&br=1007&bt=1007&cs=0&ds=3&ft=_W6LWHT8RR0sLOC3NDv2Nc0iPMgzbLUDn4-U_4d3sT_2Nv7TGW&mime_type=video_mp4&qs=0&rc=ZGloODY0NWg0NDNmOmlnOUBpajhodXU5cjkzNjMzNGkzM0BjNjYtXzUwXzMxMF4uY2BiYSM2cW5jMmQ0b21hLS1kLS9zcw%3D%3D&btag=80010e000b8001&cquery=100y&dy_q=1767927513&feature_id=dc6e471fd69cf67451806384e04f2b47&l=2026010910583343655CD359E32DDE4484'



'''#普通，没有使用stream=true和iter_conten 花费7.9s多
start_time=time.time()

r=requests.get(url=vedio_url)

Stop_time=time.time()

print(f'time={Stop_time-start_time}')

print(r.content)'''

#使用stream=true和iter_conten

r=requests.get(url=vedio_url,stream=True)

'''
如果没有目录就进行创建
'''
import os

file_path='./download/vedio'
if not os.path.exists(file_path):
    os.makedirs(file_path)


length=int(r.headers.get('Content-Length'))

'''
打开文件进行写入
'''
with open(os.path.join(file_path,'1.mp4'),'wb') as fd:
    write_all=0
    '''
    这里使用iter_content一次写100B
    '''
    for chunk in r.iter_content(chunk_size=100):
        write_all+=fd.write(chunk)
        print('下载进度 %02.26f%%'%(100*write_all/length))

