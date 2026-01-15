import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
service = Service(executable_path=path)
browser = webdriver.Chrome(service=service)

browser.get('https://movie.douban.com/top250')

ans=browser.find_elements(By.XPATH,"//*[@class='item']")

print(ans)
