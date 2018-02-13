# spider
我们所用的库主要有两个：BeautifulSoup和requests 。前者是从爬取下来的HTML文档中提起自己想要的内容，后者负责将HTML爬取下来。

  思路是这样的：先把目录上的各个章节的目录给爬取下来，保存为一个字典，然后写一个下载文章内容的函数，将所有章节的链接传到这个函数。

  我们分两段来写这段代码，首先是爬取目录的链接，其次是下载文章内容。

  爬取目录链接

[python] view plain copy
if __name__=="__main__":      
    url=r"http://www.biqule.com/book_71986/"  
    html=requests.get(url)  
    html.encoding = 'GBK'#中文  
    soup=BeautifulSoup(html.text)  
    s2=soup.find_all("dd")  
    dic={}  
    for i in s2:  
        if i.string:  
            dic[i.string]=url+i.a["href"]  
    #        print (i.string)  
    #        print (i.a["href"])  
    for i in dic.keys():  
        readbook(dic[i],i)  
这里要注意乱码问题：


这里指定的编码是gbk，所以我们也要指定编码是“GBK“

[python] view plain copy
html.encoding = 'GBK'#中文  
下载文章内容
[python] view plain copy
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
这里要注意的是读取方式要是“a+”，因为防止内存过大，所以我们直接将文章以一章一章存入。
