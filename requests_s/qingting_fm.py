import requests
import json
import re


url='https://m.qtfm.cn/rank/'

header={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1',
}
response=requests.post(url=url,headers=header)
print(response.text)
