import requests

#生成session对象
'''这里创建session对象，用来存储cookie'''
s=requests.Session()

'''第一次请求的headers中没有cookie'''
headers={
    'User-Agent':'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
}

url='https://www.baidu.com'

r=s.get(url=url,headers=headers)
print(f'请求头是{r.request.headers}')
print('='*100)
print(f'响应头体是{r.headers}')
print('='*100)
print(f'Cookie是{requests.utils.dict_from_cookiejar(r.cookies)}')
print('='*100)

'''这里是第二次进行请求，运行后打印，可以清晰的看到，这里的请求头中已经带上了cookie'''
r=s.get(url=url)
print(f'请求头是{r.request.headers}')
print('='*100)

'''如果这里依然使用session来进行请求的话，这里的cookie会来自前两个中的cookie中'''