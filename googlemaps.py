import requests
from bs4 import BeautifulSoup

url = "https://www.google.com.br/maps/search/restaurantes+em+bh/"
response = requests.get(url)
html_content = response.text 


soup = BeautifulSoup(html_content, "html.parser")

restaurants = soup.find_all("div", class_="m6QErb DxyBCb kA9KIf dS8AEf ecceSd")

for restaurant in restaurants:
    name = restaurant.find("div", class_="qBF1Pd fontHeadlineSmall ").text.strip()
    address = restaurant.find("div", class_="W4Efsd").text.strip()
    print("Name: ", name)
    print("Address: ", address)
    print("-" * 50)
