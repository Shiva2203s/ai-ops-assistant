import requests
import os

def get_weather(city: str) -> dict:
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return {
            "city": city,
            "error": "OPENWEATHER_API_KEY not set"
        }

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    # 🛟 Graceful fallback
    if "main" not in data:
        return {
            "city": city,
            "error": data.get("message", "Weather data unavailable")
        }

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }
