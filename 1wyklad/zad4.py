import asyncio


async def main() -> None:
    counter = 1
    while counter <= 5:
        print(counter)
        await asyncio.sleep(1)
        counter = counter + 1

if __name__ == "__main__":
    asyncio.run(main())