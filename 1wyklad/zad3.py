import asyncio


async def cor1() -> None:
    await asyncio.sleep(3)
    print("Hello1")

async def cor2() -> None:
    await asyncio.sleep(1)
    print("Hello2")

async def main() -> None:
    await asyncio.gather(cor1(), cor2())

if __name__ == "__main__":
    asyncio.run(main())