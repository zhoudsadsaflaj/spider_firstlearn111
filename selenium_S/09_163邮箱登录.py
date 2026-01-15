import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
service = Service(executable_path=path)

browser=webdriver.Chrome(service=service)

wait_ob=WebDriverWait(browser,10)
browser.get('https://mail.163.com/')


"""重要结论！！！

iframe 的本质：
    iframe 是 HTML 中的一个标签，作用是在当前页面中嵌入另一个独立的 HTML 文档（可以理解为 “页面套页面”）。这个嵌入的文档有自己独立的 DOM树（元素结构），和主页面的 DOM 树是分开的。
Selenium 的定位规则：
    Selenium 的 WebDriver 实例默认只 “绑定” 主页面的 DOM 树，所有元素定位操作（比如 find_element、EC.presence_of_element_located）都只会在主 DOM 树里查找。
而 163 邮箱的登录输入框，其 DOM 节点属于 iframe 内部的 DOM 树，不在主 DOM 树里，所以直接定位必然失败。
切换 iframe 的作用：
    driver.switch_to.frame(iframe) 这行代码的作用，就是把 WebDriver 的 “操作范围” 从主页面的 DOM 树，切换到 iframe 内部的 DOM 树。切换后，后续的元素定位操作就会在 iframe 的 DOM 树里执行，此时找 name="email" 就能精准匹配到输入框元素。
"""


#所以先用iframe定位
iframe = wait_ob.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
browser.switch_to.frame(iframe)
    
# 第二步：用name="email"定位（此时就能找到！）
email_input = wait_ob.until(EC.presence_of_element_located((By.NAME, 'email')))
print(email_input)

password_input=wait_ob.until(EC.presence_of_element_located((By.NAME,'password')))
print(password_input)

email_input.send_keys('18914820890')
password_input.send_keys('@ZASVBUM123')
browser.find_element(By.ID,'dologin').click()

time.sleep(10)
browser.quit()