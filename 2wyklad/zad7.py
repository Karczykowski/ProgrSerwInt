import aiohttp
import asyncio

async def fetch(url: str, location: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(location, 'wb') as file:
                file.write(await response.content.read(1024))


async def main() -> None:
    url = "https://sitechecker.pro/wp-content/uploads/2023/05/URL-meaning.jpg"
    location = r"plik.jpg"
    await fetch(url, location)


if __name__ == "__main__":
    asyncio.run(main())