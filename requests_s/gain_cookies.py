import requests

header={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1',
}

url='https://www.baidu.com'

r=requests.get(url=url,headers=header)

print(r.request.headers)
print('-'*200)
print(r.headers)
print('-'*180)
print(r.headers.get('Set-Cookie'))
print('-'*200)

print(r.cookies)
print('-'*180)

cookie=requests.utils.dict_from_cookiejar(r.cookies)
print(cookie)
print('-'*180)


