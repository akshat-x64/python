import requests
import json
query = input("Enter the name of the topic:")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-05-15&sortBy=publishedAt&apiKey=00d636948f96444689dfb6d73505996f"
aa = requests.get(url)
ab = json.loads(aa.text)
# print(ab ,type(ab))

for i in ab["articles"]:
    print(i["title"])
    print(i["description"])
    print("-----------------------------------------------------------")
