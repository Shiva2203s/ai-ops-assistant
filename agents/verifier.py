def verify_and_format(results: list) -> dict:
    final_output = {}

    for item in results:
        if item["tool"] == "github_search":
            final_output["github_repositories"] = item["output"]

        elif item["tool"] == "weather_fetch":
            final_output["weather"] = item["output"]

    if "github_repositories" not in final_output:
        final_output["github_repositories"] = []

    if "weather" not in final_output:
        final_output["weather"] = {"error": "Weather data not available"}

    return final_output
