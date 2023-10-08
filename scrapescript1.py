from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found.')
else:
    print(title)

#In this example, you’re creating a function getTitle, which returns either the title of
#the page, or a None object if there was a problem retrieving it. Inside getTitle, you
#check for an HTTPError, as in the previous example, and encapsulate two of the Beau‐
#tifulSoup lines inside one try statement. An AttributeError might be thrown from
#either of these lines (if the server did not exist, html would be a None object, and
#html.read() would throw an AttributeError). You could, in fact, encompass as
#many lines as you want inside one try statement, or call another function entirely,
#which can throw an AttributeError at any point.
