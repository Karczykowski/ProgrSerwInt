import aiohttp
import asyncio
import aiofiles
import json

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def dict_to_str(data: dict) -> str:
    return json.dumps(data, indent=4)

async def save(data: str, filename: str) -> None:
    async with aiofiles.open(filename, mode='w') as f:
        await f.write(data)

async def main() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"
    users = await fetch(url)
    str_users = await dict_to_str(users)
    await save(str_users, 'nazwaPliku.txt')

    print(users)


if __name__ == "__main__":
    asyncio.run(main())