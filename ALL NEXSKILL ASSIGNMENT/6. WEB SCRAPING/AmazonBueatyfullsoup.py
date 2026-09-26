import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"

r = requests.get(URL)

soup = BeautifulSoup(r.content,'html5lib')

smarts = []

table = soup.find('ol',attrs={'class':'a-carousel a-text-center'})

for row in table.find_all('li',
                          attrs={'class':'a-carousel-card ucw-widget-carousel-element'}):
    smart ={}
    smart['theme'] = row.h5.text
    smart['url'] = row.a['href']
    smart['img'] = row.img['src']
    smart['lines'] = row.img['alt'].split(" ")[0]
    smart['author'] = row.img['alt'].split(" ")[1]
    smarts.append(smart)