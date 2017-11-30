#-*_coding:utf8-*-
import time
from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


from selenium import webdriver
import json
dcap = dict(DesiredCapabilities.PHANTOMJS)  #设置useragent

dcap['phantomjs.page.settings.userAgent'] = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ')  #根据需要设置具体的浏览器信息

driver=webdriver.PhantomJS('D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe', desired_capabilities=dcap)

driver.get('https://list.jd.com/list.html?cat=9987,653,655')
products=driver.execute_script('return JSON.stringify(slaveWareList);')
print(products)
products=json.loads(products)
print(products)
n=0
for product in products:
    print(products[product])
    n=n+1
print(n)
driver.close()




#driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")  # Optional argument, if not specified will search path.
driver=webdriver.PhantomJS('D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe', desired_capabilities=dcap)
driver.get("https://book.jd.com/")
html = driver.page_source
#print(html)

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap[
    "phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
driver = webdriver.PhantomJS(executable_path=r'C:\Users\taojw\Desktop\pywork\phantomjs-2.1.1-windows\bin\phantomjs.exe',
                             desired_capabilities=dcap)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()



