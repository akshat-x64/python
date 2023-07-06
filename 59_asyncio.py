import asyncio
import requests

async def function1():
    print("func 1") 
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
async def function2():
    print("func 1") 
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
async def function3():
    print("func 1") 
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)



async def main():
  # await function1()
  # await function2()
  # await function3()
  # return 3
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)