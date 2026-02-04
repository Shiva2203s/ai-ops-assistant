import requests

def search_github(query: str) -> list:
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars"
    response = requests.get(url)
    data = response.json()

    repos = []
    for repo in data.get("items", [])[:3]:
        repos.append({
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"]
        })

    return repos
