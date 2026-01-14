import requests


proxy='110.43.84.217'
port=80

url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip&fenlei=256&rsv_pq=0x92a7dfcf02077702&rsv_t=92f87VHVq68h0XD8tYPrQ9%2Bn2VfKEA7c63%2FsZhtXvoAPWCH%2FYfiqwOrH8wYd&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=4&rsv_sug1=5&rsv_sug7=101&rsv_btype=i&inputT=7292&rsv_sug4=8564'

proxies={
    'http':'http://%s:%d' %(proxy,port),
    #'https':'https://%s:%d' %(proxy,port),
}

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
}

r=requests.get(url=url,headers=header,proxies=proxies)
# r.encoding='utf-8'
print(r.text)

with open('./1.html','w',encoding='utf-8') as f:
    f.write(r.text)

    