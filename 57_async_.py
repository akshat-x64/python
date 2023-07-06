import asyncio

async def function_1():
    await asyncio.sleep(3)
    print("This is run by function 1")

async def function_2():
    await asyncio.sleep(2)
    print("This is run by function 2")

async def function_3():
    await asyncio.sleep(1)
    print("This is run by function 3")


async def main():
    # l = await asyncio.gather(
    # function_1(),
    #  function_2(),
    #  function_3()

    # )
    # task1 = asyncio.create_task(function_1())
    # task2 = asyncio.create_task(function_2())
    # task3 = asyncio.create_task(function_3())
    # await task1
    # await task2
    # await task3
    await function_1()
    await function_2()
    await function_3()

asyncio.run(main())