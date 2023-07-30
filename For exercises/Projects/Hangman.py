import requests
import bs4

x = requests.get('https://randomword.com/')
text = bs4.BeautifulSoup(x.text, 'lxml')
print(text)
