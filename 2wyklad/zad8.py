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

        hour_temp = data["hourly"]["temperature_2m"]
        next_day_hour_temp = hour_temp[24:48]
        avg_temp = sum(next_day_hour_temp) / len(next_day_hour_temp)

        forecasts[city] = {
            "avg_temp_next_day": avg_temp,
            "temperature_values": next_day_hour_temp,
            "latitude": lat,
            "longitude": lon
        }

    sorted_forecasts = dict(
        sorted(forecasts.items(), key=lambda item: item[1]["avg_temp_next_day"], reverse=True)
    )
    return sorted_forecasts

async def main() -> None:
    forecasts = await forecast()
    print(forecasts)


if __name__ == "__main__":
    asyncio.run(main())