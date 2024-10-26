import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        for proba in range(3):
            try:
                async with session.get(url) as response:
                    if 200 <= response.status < 300:
                        return await response.json()
                    elif 500 <= response.status < 600:
                        print(f"Proboje jeszcze raz")
                    else:
                        return None
            except aiohttp.ClientError as e:
                print(f"Error: {e}")
    print(f"Nie udalo sie po 3 probach")
    return None


async def main() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"

    tasks = [fetch(url) for _ in range(100)]
    users = await asyncio.gather(*tasks)

    print(users)


if __name__ == "__main__":
    asyncio.run(main())