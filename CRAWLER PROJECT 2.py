import requests ,random
from bs4 import BeautifulSoup
result=requests.get("https://www.hindustantimes.com/rss/topnews/rssfeed.xml")
feed=result.text
feedsoup=BeautifulSoup(feed,"xml")
articles=[]
i=1
for item in feedsoup.find_all('item'):
	articles.append([item.find('title').text,item.find('link').text])
	print(str(i)+". "+item.find('title').text+"\n")
	i+=1
inp = int(input("\n enter article number that you wanna read? \n"))
link = articles[inp-1][1]
print (link)
# link=articles[random.randint(0,len(articles))]
result=requests.get(link)
result.encoding=result.apparent_encoding
artbod=result.text
soup=BeautifulSoup(artbod, 'html.parser')
textart = soup.title.text.strip()+"\n"
print(textart)
art = soup.find("div")
for p in art.find_all('p'):
	textart = textart + p.text.strip() + "\n"
print(textart)      
n=input("\nDO U WANT TO SAVE THIS INFORMATION IN A FILE:(y/n)")
if(n=='y'):
	f=open("output.txt","w")
	f.write(str(textart.encode('utf8')))
	f.close()
else:
	exit()
	
