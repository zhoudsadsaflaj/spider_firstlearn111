import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
service = Service(executable_path=path)
browser = webdriver.Chrome(service=service)

browser.get('https://news.baidu.com/')

time.sleep(2)

browser.find_element(By.ID,'ww').send_keys('反腐')
time.sleep(2)
browser.find_element(By.ID,'s_btn_wr').click()

time.sleep(2)