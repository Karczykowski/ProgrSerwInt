import asyncio
import random

async def fetch(delay) -> None:
    await asyncio.sleep(delay)
    print(random.randint(0,100))

async def main() -> None:
    await asyncio.gather(fetch(random.randint(0,4)), fetch(random.randint(0,4)), fetch(random.randint(0,4)))

if __name__ == "__main__":
    asyncio.run(main())