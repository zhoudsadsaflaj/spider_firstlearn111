import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
service = Service(executable_path=path)
browser = webdriver.Chrome(service=service)


browser.get('https://baidu.com')
time.sleep(5)
browser.save_screenshot('./百度页面.jpg')

browser.close()
