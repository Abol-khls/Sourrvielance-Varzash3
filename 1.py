import requests
# from bs4 import BeautifulSoup
import time 
import threading

links=[]

def get_links():
    url="https://web-api.varzesh3.com/v1.0/news/most-visited?includeSports[0]=Football&includeSports[1]=Futsal&includeSports[2]=BeachSoccer"

    web = requests.get(url)
    data = web.json()
    for datum in data:
        if datum["link"] not in links:
            links.append(datum["link"])
    with open("links.txt", "wt",encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")
        
  
get_links()



with open("links.txt", "wt",encoding="utf-8") as f:
    for link in links:
        f.write(link + "\n")
        
st = time.time()
t=0

while True:
    tt= time.time()
    t+=tt-st
    st=tt
    if t> 120:
        
        th=threading.Thread(target= get_links)
        th.start()
        print("thread")

        t=0