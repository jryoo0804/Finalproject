import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#baseUrl = 'https://search.shopping.naver.com/search/all.nhn?query='
plusUrl = urllib.parse.quote_plus(input('검색어를 입력하세요: '))
#Url = baseUrl + urllib.parse.quote_plus(plusUrl)

pageNo=1
url = f'https://search.shopping.naver.com/search/all.nhn?origQuery={plusUrl}&pagingIndex={pageNo}&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query={plusUrl}'

data = requests.get(url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
titles = soup.select(".link")

for i in titles:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()

pageNo+=1

#names = soup.select(".link")
#title_names = [title.text for title in names]
#title_links = [title["href"] for title in names]
#list_total = [title_names, title_links]
#df = pd.DataFrame(list_total).T
#print(df)






