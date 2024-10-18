import asyncio


async def A() -> None:
    while True:
        await asyncio.sleep(2)
        print("Maszyna A skonczyla")


async def B() -> None:
    while True:
        await asyncio.sleep(3)
        print("Maszyna B skonczyla")


async def C() -> None:
    while True:
        await asyncio.sleep(5)
        print("Maszyna C skonczyla")


async def main() -> None:
    try:
        await asyncio.wait_for(asyncio.gather(A(), B(), C()), timeout=15)
    except asyncio.TimeoutError:
        print("Czas działania maszyn się zakończył")


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())