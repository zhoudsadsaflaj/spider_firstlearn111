import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
service = Service(executable_path=path)
browser = webdriver.Chrome(service=service)

browser.get('http://www.baidu.com')

print(browser.page_source)
print(browser.get_cookies())
print(browser.current_url)

time.sleep(10)

browser.quit()

