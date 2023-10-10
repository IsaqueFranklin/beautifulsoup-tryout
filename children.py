from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table', {'id': 'giftList'}).descendants:
    print(child)

#All the descendents are inside a tag, but the children is the element right below the tag => children
#So all children are descendents but only one descendent is the children => descendents
#Sibiling objects with the tag => next_siblings