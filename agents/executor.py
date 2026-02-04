from tools.github_tool import search_github
from tools.weather_tool import get_weather

def execute_plan(plan: dict) -> list:
    results = []

    for step in plan["steps"]:
        tool = step["tool"]
        input_value = step["input"]

        if tool == "github_search":
            results.append({
                "tool": "github_search",
                "output": search_github(input_value)
            })

        elif tool == "weather_fetch":
            results.append({
                "tool": "weather_fetch",
                "output": get_weather(input_value)
            })

    return results
