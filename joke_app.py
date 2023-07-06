import requests
import json
import time
url = "https://v2.jokeapi.dev/joke/Programming,Dark?blacklistFlags=religious,political&amount=10"
aa = requests.get(url)
# print(aa.text)
final = json.loads(aa.text)
i = 1
aa = "jokes"
for i in final["jokes"]:
    # print(aa,i)
    if i["type"] == "single":
        print(i["joke"])
    elif i["type"] == "twopart":
        print(i["setup"])
        time.sleep(5)
        print(i["delivery"])
    time.sleep(5)
    i = i+1
    print("------------------------------------------------")
