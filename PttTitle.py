import urllib.request as req
from http.client import responses
url='https://www.ptt.cc/bbs/movie/index.html'
#建立一個Request物件,附加Request Headers的資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Iron Safari/537.36"})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

#解析原始碼,取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,'html.parser')#讓BeautifulSoup協助我們解析HTML格式文侔
titles=root.find_all('div',class_='title')#尋找所有class='title'的div標籤
for title in titles :
 if title.a != None:#如果標題包含 a標籤(沒有被刪除).印出來
     print(title.a.string)
print(title.a.string)
