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

async def forecast(cities: dict, mask: dict) -> dict:

    forecasts = {}

    for city, (lat, lon) in cities.items():
        data = await weather(lat, lon)
        data = data["hourly"]
        key = next(iter(mask))
        val = data[key][0]

        operator, num = mask[key].split()
        if eval(f"{val}{operator}{num}"):
            forecasts[city] = {
                "temperature": data["temperature_2m"][0],
                "wind_speed": data["wind_speed_10m"][0],
                "time": data["time"][0]
            }

    return forecasts

async def main() -> None:
    cities = {
        "Porlamar": (10.5728, -63.5056),
        "Moroni": (-11.4277, 43.1518),
        "Helsinki": (60.1920, 24.9458)
    }
    mask = {
        "wind_speed_10m": "< 20"
    }

    forecasts = await forecast(cities, mask)
    print(forecasts)


if __name__ == "__main__":
    asyncio.run(main())