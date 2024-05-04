import time
import asyncio
import random


async def marriage(name):
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"{name} married after {r} years.")


async def main():
    await asyncio.gather(marriage("Ali"), marriage("Mike"), marriage("Hassan"), marriage("Sara"))


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter() - start
    print(f"Executed in {end} seconds.")