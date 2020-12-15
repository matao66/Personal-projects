#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pandas import DataFrame
browse=webdriver.Chrome()#这个单独一行




# In[13]:


def web(www):             #定义一个获取网页的函数
    browse.get(www)       #打开一个网址
    Tao_name=[]           #获取商品的名字
    for i in browse.find_elements_by_class_name('J_ClickStat'):
        Tao_name.append(i.text)
        Tao_name1=sorted(set(Tao_name),key=Tao_name.index)    #注意这里一条数据占用了两行，我采用取奇数行的方式
    del Tao_name1[0]            #第一行为空删掉
    Tao_count=[]                    #获取购买的数量
    for i in browse.find_elements_by_class_name('deal-cnt'):
        Tao_count.append(i.text)
    Tao_price=[]
    for i in browse.find_elements_by_xpath('//div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]/div[1]/div[1]'):
        Tao_price.append(i.text)      #上一行我用的是'by_xpath',因为价格是动态网页
    Taobao=DataFrame()                    #用DataFrame()保存数据
    Taobao['名字']=Tao_name1
    Taobao['购买量']=Tao_count
    Taobao['价格']=Tao_price
    return Taobao




def page(n):               # 定义一个获取页数的函数      
    Taobao=DataFrame()     
    for j in range(n): 
        Tao_web='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E6%89%8B%E6%9C%BA&suggest=history_1&_input_charset=utf-8&wq=meishi&suggest_query=meishi&source=suggest&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s={}'.format(j*44) 
        #print(aaaa) 
#         ='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E7%BE%8E%E9%A3%9F&suggest=history_1&_input_charset=utf-8&wq=meishi&suggest_query=meishi&source=suggest&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s={}'.format(j*44) 
        df_page=web(Tao_web) #上一页：利用format() 获取多页    本页：打开这个网址
        Taobao=Taobao.append(df_page,ignore_index=True)    #多页数据拼接
    return Taobao 



