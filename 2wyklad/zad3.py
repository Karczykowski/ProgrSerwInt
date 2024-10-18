
import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def str1() -> None:
    url = "https://api.github.com/users/hadley/orgs"
    users = await fetch(url)

    print(users)

async def str2() -> None:
    url = "https://api.github.com/users/hadley/repos"
    users = await fetch(url)

    print(users)

async def str3() -> None:
    url = "https://api.github.com/repos/hadley/ggplot2/commits"
    users = await fetch(url)

    print(users)

async def str4() -> None:
    url = "https://api.github.com/repos/hadley/ggplot2/issues"
    users = await fetch(url)

    print(users)

async def str5() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"
    users = await fetch(url)

    print(users)

async def main() -> None:
    await asyncio.gather(str1(), str2(), str3(), str4(), str5())

if __name__ == "__main__":
    asyncio.run(main())