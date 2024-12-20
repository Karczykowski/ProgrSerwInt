import asyncio


async def main() -> None:
    await asyncio.sleep(2)
    print("Hello world!")


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())