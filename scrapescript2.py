#web scrapper to select elements acording to their color classes.
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        nameList = bs.find_all('span', {'class': 'green'})
    except AttributeError as e:
        return None
    return nameList

nameList = getTitle('http://www.pythonscraping.com/pages/page1.html')
if nameList == None:
    print('Title could not be found.')
else:
    for name in nameList:
        print(name.get_text())