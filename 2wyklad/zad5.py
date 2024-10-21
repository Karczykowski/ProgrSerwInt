import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def weather(latitude: float, longitude: float) -> dict:
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
        "&hourly=temperature_2m,wind_speed_10m"
    )
    return await fetch(url)

async def forecast() -> dict:
    cities = {
        "Porlamar": (10.5728, -63.5056),
        "Moroni": (-11.4277, 43.1518),
        "Helsinki": (60.1920, 24.9458)
    }

    forecasts = {}

    for city, (lat, lon) in cities.items():
        data = await weather(lat, lon)

        hour = data["hourly"]

        temperature = hour["temperature_2m"][0]
        wind_speed = hour["wind_speed_10m"][0]

        forecasts[city] = {temperature, wind_speed}

    return forecasts

async def main() -> None:
    forecasts = await forecast()
    print(forecasts)


if __name__ == "__main__":
    asyncio.run(main())