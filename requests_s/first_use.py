import requests
#学会使用requests发送请求，获得响应，在对响应进行处理


url='https://www.baidu.com'

response=requests.get(url=url)
'''
    requests 包括：
        get、post、put、delete、option等方法
        这里使用get来请求
        同时返回一个对象，用response来接收，之后可以对response进行操作

    操作：
        1、status_code 可以提取状态码
        2、text、content可以提取内容,可以对这里的内容进行保存存储
        3、通过使用utf-8编码解码可以看到数据
'''


print('-----状态码-----')
print(response.status_code)

print('-----bytes类型数据-----')
print(response.content)#返回二进制串b'' 这里主要来拿视频音频
#print(response.text)   这里得到是str类型，所以中文乱码，text主要来拿文本

print('-----str类型数据-----')
response.encoding='utf-8'
print(response.text)

print('-----str类型数据（utg-8）-----')
print(response.content.decode('utf-8'))