from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(child)

#Regex are used to identify regular strings.
#What is a regular string?It’s any string that can be generated by a series of linear rules, such as these:
#Write the letter a at least once
#Append to this the letter b exactly five times
#Append to this the letter c any even number of times
#Write either the letter d or e at the end