import requests

url='http://www.baidu.com'

header={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1',
}

r=requests.get(url=url,headers=header)

print(r.status_code)
print(r.url)#最后一次请求的url，这就是重定向
print('-'*180)

'''
    有的时候，我们不希望重定向，这时候在函数中加上allow_redirection=False
'''
r=requests.get(url=url,headers=header,allow_redirects=False)

print(r.status_code)
print(r.url)#最后一次请求的url
print('-'*180)

#如果自己想去找重定向的网址，则需要自己找，在headers中的Location中
print(r.headers.get('Location'))


r1=requests.get(url=r.headers.get('Location'),headers=header,allow_redirects=False)
print(r1.status_code)
print(r1.headers.get('Location'))
print('-'*180)

'''
    这里有一个.history函数可以看到跳转记录
'''
r=requests.get(url=url,headers=header)
print('history-->',r.history)

#可以看出这里返回的是一个对象，故可以迭代这个对象
def iter_history():
    count=1
    for one_info in r.history:
        print(f'====={count}个跳转=====')
        print(one_info.status_code,one_info.url,one_info.headers,sep='\n')
        count+=1

iter_history()
print('-'*180)

