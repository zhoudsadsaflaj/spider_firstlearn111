import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
service = Service(executable_path=path)
browser = webdriver.Chrome(service=service)

browser.get('https://www.baidu.com')

time.sleep(2)

js='window.open("https://www.jd.com")'
browser.execute_script(js)

time.sleep(3)

browser.switch_to.window(browser.window_handles[0])
time.sleep(2)
browser.switch_to.window(browser.window_handles[1])
time.sleep(2)
browser.close()
time.sleep(2)
browser.close()
