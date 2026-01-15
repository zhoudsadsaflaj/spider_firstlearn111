import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
service = Service(executable_path=path)
browser = webdriver.Chrome(service=service)

from selenium.webdriver.common.by import By
browser.get('https://www.baidu.com')

browser.find_element(By.ID,'chat-textarea').send_keys('china')
browser.find_element(By.ID,'chat-submit-button').click()

time.sleep(100)
browser.quit()