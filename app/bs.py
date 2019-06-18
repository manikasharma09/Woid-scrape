import requests 
from bs4 import BeautifulSoup 
import csv 

def func():  
    URL = "http://digg.com/"
    r = requests.get(URL) 
  
    soup = BeautifulSoup(r.content, 'lxml')
    soup1 = soup.findAll('h2',itemprop='headline') 
    soup2= soup.find('h2',class_='digg-story__title entry-title')
    #print(soup2)
    a=[]
    c=0
    for i in soup1:
        c=c+1
        if(c==3):
            break
        else:
            s=i.text
            a.append(s)
    return a

def func1():  
    URL = "https://medium.com/"
    r = requests.get(URL) 
  
    soup = BeautifulSoup(r.content, 'lxml')
    soup2= soup.findAll('div',class_='extremeHero-smallCardContainer')
    ar=[]
    for i in soup2:
        head=i.findAll('article')
        for j in head:
            ar.append(j.text)
    return ar

