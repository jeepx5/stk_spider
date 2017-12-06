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
import tushare as ts
import pandas as pd
import random


df=ts.get_stock_basics()
df.to_csv('.\stk_basic.csv')#, encoding='utf-8')
#df=pd.read_csv('.\stk_basic.csv')
clst=df.index.tolist()
#clst=df['code'].tolist()
print(clst)


time.sleep(5)
urlbase = 'http://money.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/'
urltail = '/displaytype/30.phtml'

#codelst=['000528', '600006', '002426']
codelst=clst
stkhld = {}



for code in codelst:
    url = urlbase + str(code) + urltail
    print(url)
    spider = stk_hld()
    stkhld[code] = spider.stk_hld_scrapy(url, code)
    rnd=random.gauss(25, 13)
    time.sleep(rnd)




print(stkhld)
print(stkhld.keys())
stk_df=pd.DataFrame.from_dict(stkhld, orient='index', dtype=None)
stk_df.to_csv('.\stkhold.csv')
