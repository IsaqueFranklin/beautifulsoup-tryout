from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import random
import re

random.seed(datetime.now().timestamp())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div',  {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

#Parei na página 54 do livro de webscrapping
#https://www.scaler.com/topics/python/encapsulation-in-python/