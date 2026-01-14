import requests

headers={
    'User-Agent':'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
}

url='https://fanyi.baidu.com/sug'

payload={
    'kw':'password'
}

'''所以这里具体使用什么格式，需要看浏览器中具体是form data，还是json格式，然后具体再进行选择'''

'''通过运行之后可以看到，如果传入的是data，则请求头中 Content-Type=application/x-www-form-urlencoded，且请求体是kw=password'''

r=requests.post(url=url,headers=headers,data=payload)
print(f'请求头是{r.request.headers}')
print(f'请求体是{r.request.body}')

print('='*100)

'''通过运行之后可以看到，如果传入的是json，则请求头中 Content-Type=application/json，且请求体是b\'{"kw": "password"}\''''

r=requests.post(url=url,headers=headers,json=payload)
print(f'请求头是{r.request.headers}')
print(f'请求体是{r.request.body}')
print(r.json)
print('='*100)