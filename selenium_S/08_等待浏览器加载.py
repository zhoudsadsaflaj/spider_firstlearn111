import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
service = Service(executable_path=path)

browser=webdriver.Chrome(service=service)

browser.get('https://www.jd.com')

wait_ob=WebDriverWait(browser,5)

search_input=wait_ob.until(EC.presence_of_element_located((By.ID,'key')))
print(search_input)

search_input.send('MAC pro')
time.sleep(3)

browser.close()
