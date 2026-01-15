import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
service = Service(executable_path=path)
browser = webdriver.Chrome(service=service)

browser.get('https://www.baidu.com')

cookies_list=browser.get_cookies()
print(cookies_list)

cookie_dict={x['name']:x['value'] for x in cookies_list}

print(cookie_dict)