from select import select
import requests
from bs4 import BeautifulSoup
import soupsieve 
url = 'https://www.ptt.cc/bbs/MobileComm/index.html'
r = requests.get(url)
# 網頁get下來

soup = BeautifulSoup(r.text,"html.parser")

sel = soup.select("div.title a")

for i in sel:
    print( f'Link is :{url - index.html +str(i["href"])}\nTitle is :{i.text}') 
# 注意f-string "" 與'' 否則會抱錯f-string: unmatched '['