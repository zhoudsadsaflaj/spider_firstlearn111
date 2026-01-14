import requests
import json

url='https://gate.lagou.com/v1/entry/positionsearch/searchPosition/v2'

header={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1',
}

response=requests.get(url=url,headers=header)
json_str=response.content.decode()
json_dict=json.loads(json_str)
print(json_dict)