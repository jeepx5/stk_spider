#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
from urllib import request
from urllib import parse
import pandas as pd
import numpy as np
import time
import random


def filter_tags(htmlstr):
    # 先过滤CDATA
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 处理换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    # 去掉多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    return s





urlbase='http://www.dianping.com/search/category/1/75/g3030p'


def extFeature(item, cname, content):
    rst = item.find_all(cname, class_=content)
    return rst




def remChar(str, lst):
    a=str
    for char in lst:
        a=a.replace(char,'')
    return a

def getDetail(lnk):
    headers = {
      'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
      'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
      'Connection': 'keep-alive'}
    ip = ['121.31.159.197', '175.30.238.78', '124.202.247.110']
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
               'X-Forwarded-For': ip[random.randint(0, 2)]}
    req = request.Request(lnk, headers=headers)
    page = request.urlopen(req).read()
    #page = page.decode('utf-8')
    print(page.decode('utf-8'))
    soup = BeautifulSoup(page)
    raw_add=soup.find_all('div', class_='address')
    address=remChar(str(raw_add[0]), ['<div class="address">', '<span class="item">地址：</span>', '</div>', '\s+'])
    print(address)
    lst = []
    for item in soup.find_all('span', class_='item'):
        if 'J-phone-hide' in str(item):
            pass
        rateNum=remChar(str(item), ['<span class="item">', '</span>', '<i class="icon-shop">', '</i>'])
        lst.append(rateNum)
        print(rateNum)




def getList(url):
    response = request.urlopen(url)
    page = response.read()
    soup = BeautifulSoup(page)
    shlst={}
    for item in soup.find_all('div', class_='tit'):
        ptlnk=re.compile('http:.+#reserve')
        shopname=item.find_all('h4')
        ptname=re.compile(r'>.+<')
        shname=re.findall(ptname, str(shopname))[0]
        shname = remChar(shname, ['>', '<'])
        print(shname)
        #print(item)
        lnk=item.find_all('a', class_='ibook')
        #print(item)
        #lnk = item.find_all('a', title_=shname)
        #if len(lnk) !=1 : continue
        print(lnk)
        link=re.findall(ptlnk, str(lnk))
        lnk=remChar(link[0], ['href="', '"'])
        shlst[shname] = lnk

        ratenum = extFeature(item, 'a', 'review-num')
        print(ratenum)

    print(shlst)
    return shlst



def extList(url):
    response = request.urlopen(url)
    page = response.read()
    page = page.decode('utf-8')
    soup = BeautifulSoup(page)
    shlst={}
    for item in soup.find_all('div', class_='txt'):
        #get name
        nlst = extFeature(item, 'div', 'tit')
        ptname=re.compile(r'h4>.+<')
        shname=re.findall(ptname, str(nlst))[0]
        shname = remChar(shname, ['h4>', '<'])
        print(shname)
        #get address
        alst = extFeature(item, 'div', 'tag-addr')
        ptaddr = re.compile(r'<span class="addr">.+</span>')
        adname = re.findall(ptaddr, str(alst))
        addrname = remChar(adname[0], ['<span class="addr">', '</span>'])
        #print(addrname)
        #get score
        numlst = extFeature(item, 'div', 'comment')
        ptnum = re.compile(r'sml-str.+"')
        nscore = re.findall(ptnum, str(numlst))
        score = remChar(nscore[0], ['sml-str', 'title="', '"'])
        #print(score)
        #get tot
        totlst = extFeature(item, 'b', '') #reviewnum, price, effect, teacher, env
        tot = []
        for i in totlst:
            tot.append(remChar(str(i), ['<b>', '</b>']))
        if len(tot)<5: tot.insert(1, 'na')
        tot.append(score)
        tot.append(addrname)
        #print(tot)
        shlst[shname]=tot
        #print(shlst)

    return shlst




shlst={}


for i in range(1,27):
    url = urlbase+str(i)
    shlst = dict(shlst, **extList(url))
    time.sleep(1)
print(len(shlst.keys()))

df=pd.DataFrame.from_dict(shlst,orient='index')
df.rename(columns={'0':'shop', '1':'rateNum', '2':'meanprice', '3':'effect', '4':'teacher', '5':'env', '6':'address'}, inplace = True)
df.columns=['shop', 'rateNum', 'meanprice', 'effect', 'teacher', 'env', 'address']
print(df)
df.to_csv('eng_org2.csv')
