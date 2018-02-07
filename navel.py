# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests 
import sys   
import bs4
sys.setrecursionlimit(1000000) #例如这里设置为一百万

def readbook(url,title):
    txt=[]
    #读取方式为w，如果以二进制读取，可能会出现TypeError: a bytes-like object is required, not 'str'错误
    #a+     以读写模式打开
    f=open(r"C:\Users\asus-pc\Desktop\book.txt","a+")
    f.write(title)
    html=requests.get(url,timeout = 500)
    html.encoding = 'GBK'#中文
    soup=BeautifulSoup(html.text)
    s=soup.select("#content")
    for i in s[0]:     
        if type(i)==bs4.element.NavigableString:        
            txt.append(str(i))
    for i in txt[1::2]:
        f.write(i.replace(u'\xa0', u' '))
    f.close()
    
if __name__=="__main__":    
    url=r"http://www.biqule.com/book_71986/"
    html=requests.get(url)
    html.encoding = 'GBK'#中文
    soup=BeautifulSoup(html.text)
    #s1=soup.select("body > div:nth-of-type(3)")
    #@使用BeautifulSoup对html解析时，当使用css选择器，对于子元素选择时，要将nth-child改写为nth-of-type才行，
    #
    #如  ul:nth-child(1)   应该写为   ul:nth-of-type(1)   
    s2=soup.find_all("dd")
    dic={}
    for i in s2:
        if i.string:
            dic[i.string]=url+i.a["href"]
    #        print (i.string)
    #        print (i.a["href"])
    for i in dic.keys():
        readbook(dic[i],i)