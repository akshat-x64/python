import requests
from bs4 import BeautifulSoup
respone = requests.get("https://www.codewithharry.com/blog")
# print(respone.text)


url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
harry = requests.get(url)

soup = BeautifulSoup(harry.text,"html.parser")
# print(soup)


for heading in soup.findAll("h2"):
    print(heading.text)