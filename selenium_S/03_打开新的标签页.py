import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
service = Service(executable_path=path)
browser = webdriver.Chrome(service=service)

browser.get('https://www.baidu.com')

time.sleep(2)

browser.get('https://www.jd.com')
time.sleep(3)

browser.close()