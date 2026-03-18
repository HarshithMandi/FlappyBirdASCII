import asyncio

async def async_function():
    print("M1")
    await asyncio.sleep(2)
    print("M2")
    await asyncio.sleep(2)
    print("M3")

asyncio.run(async_function())
print("finished")