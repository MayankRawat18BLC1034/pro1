import requests ,random
from bs4 import BeautifulSoup
result=requests.get("https://www.hindustantimes.com/rss/topnews/rssfeed.xml")
feed=result.text
feedsoup=BeautifulSoup(feed,"xml")
articles=[]
for item in feedsoup.find_all('item'):
    articles.append(item.find('link').text)
link=articles[random.randint(0,len(articles))]
result=requests.get(link)
result.encoding=result.apparent_encoding
artbod=result.text
soup=BeautifulSoup(artbod, 'html.parser')
print(soup.title.text.strip())
art = soup.find("div")
for p in art.find_all('p'):
    print(p.text.strip())      
n=input("\nDO U WANT TO SAVE THIS INFORMATION IN A FILE:(y/n)")
if(n=='y'):
    f=open("output.txt","a")
    print(soup.title.text.strip(),file=f)
    for p in art.find_all('p'):
        print(p.text.strip(),file=f)
    f.close()
else:
    exit()
    
