import asyncio

async def fun1():
    print("T1")
    await asyncio.sleep(2)
    print("T1'")


async def fun2():
    print("T2")
    await asyncio.sleep(2)
    print("T2'")

async def main():
    await asyncio.gather(fun1(),fun2())

asyncio.run(main())