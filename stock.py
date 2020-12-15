#!/usr/bin/env python
# coding: utf-8

# In[22]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pandas import DataFrame
import pandas as pd



from selenium import webdriver

browse=webdriver.Chrome()
browse.implicitly_wait(10)



aa=pd.read_excel(r"C:\Users\CDA\Desktop\项目大全\金融爬虫\交通运输、仓储和邮政业 (2).xlsx")


bb=aa.iloc[:,0]

for i in bb: 
    if len(str(i))==4:
#     mm='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E7%BE%8E%E9%A3%9F&suggest=history_1&_input_charset=utf-8&wq=meishi&suggest_query=meishi&source=suggest&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s={}'.format(j*44) 
    #print(aaaa) 
        mm='http://quotes.money.163.com/f10/lrb_00{}.html?type=year'.format(i) 
        mm2.append(mm)
    elif len(str(i))==3:
        
        mm='http://quotes.money.163.com/f10/lrb_000{}.html?type=year'.format(i) 
        mm2.append(mm)
    else:
        mm='http://quotes.money.163.com/f10/lrb_{}.html?type=year'.format(i) 
        mm2.append(mm)


gupiaoming=[]
for i in mm2: 
    
    try:
        browse.get(i)
        if (browse.find_element_by_xpath('//*[@id="scrollTable"]/div[4]/table/tbody/tr[26]/td[1]').text != '--') or(browse.find_element_by_xpath('//*[@id="scrollTable"]/div[4]/table/tbody/tr[26]/td[2]').text!= '--')or(browse.find_element_by_xpath('//*[@id="scrollTable"]/div[4]/table/tbody/tr[26]/td[3]').text!= '--')or(browse.find_element_by_xpath('//*[@id="scrollTable"]/div[4]/table/tbody/tr[26]/td[4]').text!= '--')or(browse.find_element_by_xpath('//*[@id="scrollTable"]/div[4]/table/tbody/tr[26]/td[5]').text!= '--')or(browse.find_element_by_xpath('//*[@id="scrollTable"]/div[4]/table/tbody/tr[26]/td[6]').text!= '--'):
            browse.find_element_by_xpath('//*[@id="downloadData"]').click()

            ab=browse.find_element_by_xpath('//*[@id="menuCont"]/ul/li[1]/a').text
            gupiaoming.append(ab)
            browse.find_element_by_xpath('//*[@id="menuCont"]/div/div[3]/ul/li[4]/a').click()
            browse.find_element_by_xpath('//*[@id="scrollTable"]/ul/li[2]/a').click()
            browse.find_element_by_xpath('//*[@id="downloadData"]').click()
            browse.find_element_by_xpath('//*[@id="menuCont"]/div/div[3]/ul/li[6]/a').click()
            browse.find_element_by_xpath('//*[@id="scrollTable"]/ul/li[2]/a').click()
            browse.find_element_by_xpath('//*[@id="downloadData"]').click()
        else:
            print('1234')
        
    except:
        continue






