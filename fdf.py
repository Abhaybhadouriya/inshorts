import requests
from bs4 import BeautifulSoup as bs
import json
import io

value="sports"
if(value=='all'):
        r=requests.get("https://inshorts.com/en/read").text
else:
        r=requests.get("https://inshorts.com/hi/read/"+value).text
        soup=bs(r,'lxml')
        x=soup.find_all('div',class_="news-card z-depth-1")
        val={}
        val["data"]=[]
        for i in range(0,len(x)):
            dic={}
            dic["title"]=x[i].find('span', itemprop="headline").text
            dic["decription"]=x[i].find('div',itemprop="articleBody").text
            print x[i].find('div',itemprop="articleBody").text.encode('utf8')
            dic["images"]=x[i].find('div', class_="news-card-image")['style'].split("url(")[1].split(")")[0].replace("'",'')
            dic["author"]=x[i].find('span',class_='author').text
            dic["time"]=x[i].find('div', class_="news-card-author-time news-card-author-time-in-content").text.splitlines(2)[2].replace("      ","").rstrip()
            dic["inshorts-link"]=x[i].find('span',content="")['itemid']
            if(x[i].find('a', class_="source")==None):
                dic["read-more"]="None"
            else:
                dic["read-more"]=x[i].find('a', class_="source").attrs['href']
            val["data"].append(dic)
        val["category"]=value
        val["count-articles"]=len(x)
#        with io.open('data.json', 'w',encoding="utf-8") as f:
#                                       f.write(unicode(json.dumps(val, ensure_ascii=False)))
                            
