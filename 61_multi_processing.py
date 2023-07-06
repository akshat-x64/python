import multiprocessing
import requests


url = "https://picsum.photos/2000/3000"
def downloadFile(url,name):
    response = requests.get(url,name)
    open(f"{name}.jpg" ,'wb').write(response.content)
    pass


pros = []
for i in range(5):
    # downloadFile(url,str(i))
    p = multiprocessing.Process(target=downloadFile,args=[url,str(i)])
    p.start()
    pros.append(p)



for p in pros:
    p.join()
