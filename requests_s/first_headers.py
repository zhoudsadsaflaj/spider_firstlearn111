import requests

headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1',
    'Cookie':'ttwid=1%7CgnjEnDetTlTrpoD9znR5WibshkMnEXg0zWer-e8nBwU%7C1767921704%7Ce1e3be3172e42ac7f717e011f58904c504e006b98f67a26e446c3293e2fb68de; gfkadpd=1243,16720; _tea_utm_cache_1243={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22ios%22%2C%22utm_campaign%22:%22client_share%22}',
}

r=requests.get('https://wwwbaidu.com',headers=headers)


#响应头
print('type(headers)-->',type(r.headers))
print('headers->>',r.headers)

print('\n\n\n\n')

#请求头
print('type(request.headers-->)',type(r.request.headers))
print('request.headers-->',r.request.headers)
