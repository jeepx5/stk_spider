#-*_coding:utf8-*-
import time
from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from spider_stk_hld import stk_hld

urlbase = 'http://money.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/'
urltail = '/displaytype/30.phtml'

codelst=['000528', '600006', '002426']

stkhld = {}



for code in codelst:
    url = urlbase + code + urltail
    print(url)
    spider = stk_hld()
    stkhld[code] = spider.stk_hld_scrapy(url, code)

print(stkhld)
print(stkhld.keys())
