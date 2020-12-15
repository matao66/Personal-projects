#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pandas import DataFrame




browse.implicitly_wait(2)


browse=webdriver.Chrome()

browse.get('https://www.douban.com/doulist/1641439/?start=0&sort=seq&playable=0&sub_type=')


browse.find_element_by_xpath('//*[@id="item786101796"]/div/div[2]/div[4]/a').text



browse.find_element_by_xpath('//*[@id="item786101796"]/div/div[2]/div[6]').text


def web(www):             #定义一个获取网页的函数
    browse.get(www)       #打开一个网址
    bb=[]
    for i in browse.find_elements_by_xpath('//*[@class="title"]/a'):
        bb.append(i.text)
             #获取购买的数量
    bb2=[]
    for i in browse.find_elements_by_xpath('//*[@class="abstract"]'):
        bb2.append(i.text)
    bb3=[]
    for i in browse.find_elements_by_xpath('//*[@class="comment"]'):
        bb3.append(i.text)
    
         #上一行我用的是'by_xpath',因为价格是动态网页
    Taobao=DataFrame()                    #用DataFrame()保存数据
    Taobao['名字']=bb
    Taobao['购买量']=bb2
    Taobao['票房']=bb3
    return Taobao



def page(n):               # 定义一个获取页数的函数      
    Taobao=DataFrame()     
    for j in range(n): 
        try:
            Tao_web='https://www.douban.com/doulist/1641439/?start={}&sort=seq&playable=0&sub_type='.format(j*25) 
            #print(aaaa) 
    #         ='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E7%BE%8E%E9%A3%9F&suggest=history_1&_input_charset=utf-8&wq=meishi&suggest_query=meishi&source=suggest&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s={}'.format(j*44) 
            df_page=web(Tao_web) #上一页：利用format() 获取多页    本页：打开这个网址
            Taobao=Taobao.append(df_page,ignore_index=True)    #多页数据拼接
        except:
            pass
    return Taobao 



a.to_csv(r"C:\Users\CDA\Desktop\项目大全\迪士尼动画项目\全球票房数据.csv")


for j in range(4): 
       Tao_web='https://www.douban.com/doulist/1641439/?start={}&sort=seq&playable=0&sub_type='.format(j*25) 
       print(Tao_web)







