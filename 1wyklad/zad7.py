import asyncio


async def krojenie() -> None:
    await asyncio.sleep(2)
    print("Pokrojono")

async def smazenie() -> None:
    await asyncio.sleep(1)
    print("Wysmazono")

async def gotowanie() -> None:
    await asyncio.sleep(3)
    print("Ugotowano")

async def danie1() -> None:
    await gotowanie()
    await gotowanie()
    await smazenie()
    print("Ugotowano danie1")

async def danie2() -> None:
    await smazenie()
    await krojenie()
    await smazenie()
    print("Ugotowano danie2")

async def danie3() -> None:
    await krojenie()
    await smazenie()
    await gotowanie()
    print("Ugotowanie danie3")

async def main() -> None:
    await asyncio.gather(danie1(), danie2(), danie3())
    
if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())