import requests
import json

url='https://fanyi.baidu.com/sug'

header={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1'
}

payload={
    'kw':'try'
}

r=requests.post(url=url,headers=header,data=payload)

#这里返回的是一个长得字典的字符串
print(r.text)

print('-'*20)


#可以用json.dumps（字典）--->json字符串
#这里用json中的loads函数将这个字符串变成字典
q=json.loads(r.text)
print(q)


print('-'*20)

k=q.get('data')[0].get('k')
print(k)
print('-'*20)

v=q.get('data')[0].get('v')
print(v)
print('-'*20)
