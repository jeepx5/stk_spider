#-*_coding:utf8-*-
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import json


class stk_hld():
    def __init__(self):
        pass

    def stk_hld_scrapy(self, url, code):
        dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置useragent
        dcap['phantomjs.page.settings.userAgent'] = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ')  # 根据需要设置具体的浏览器信息
        driver = webdriver.PhantomJS('D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe', desired_capabilities=dcap)
        driver.get(url)
        xpth_table = '/html/body/div[@id="wrap"]/div[@id="main"]/div[@id="center"]/div[@class="centerImgBlk"]/div[@id="con02-2"]/table[@id="Table1"]/tbody'
        products = driver.find_element_by_xpath(xpth_table).text
        if len(products) >0:
            print('data obtained. Ready to parse')
        else:
            print('no data obtained, please check the internet connection')
        stk_hld = {'date':[],
                   'name': [],
                   'num': [],
                   'ratio': [],
                   'type': []
                    }
        m = 1
        i = 0
        for item in products.split('\n'):
            case = str(m)
            if '20' in item:
                stk_hld['date'].append(item)
                print(item)

            #print(case)
            if item == case:
                print(str(m / 10 * 100) + '%')
                m += 1
                # print(products.split('\n')[i+1])
                stk_hld['name'].append(products.split('\n')[i + 1])
                stk_hld['num'].append(products.split('\n')[i + 2])
                stk_hld['ratio'].append(products.split('\n')[i + 3])
                stk_hld['type'].append(products.split('\n')[i + 4])
                if m==11:
                    break
            i += 1


            # print(item)
        stok_hld={code: stk_hld}
        print('\n========data extracted==========')
        return stk_hld





