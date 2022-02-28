import requests
from bs4 import BeautifulSoup
import json


url = 'https://diphis.ru/1000-tsitat.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span')


quotesList=[]
quoteItem1={}
for quote in quotes:
    print(quote.text)
    del quoteItem1
    quoteItem1={}
    quoteItem1['text']=str(quote.text)
    quoteItem1['trans']=""
    quoteItem1['author']=""
    
    quotesList.append(quoteItem1)

jsonString = json.dumps(quotesList, ensure_ascii=False)
jsonFile = open("data2.json", "w", encoding="UTF-8")
jsonFile.write(jsonString)
jsonFile.close()