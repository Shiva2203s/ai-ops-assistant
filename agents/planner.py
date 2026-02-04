import json
from llm.client import ask_llm

SYSTEM_PROMPT = """
You are a Planner Agent.

Your task is to convert the user request into a JSON execution plan.

STRICT RULES:
- Output ONLY valid JSON
- Do NOT include explanations, markdown, or extra text
- Follow this schema EXACTLY:

{
  "steps": [
    { "tool": "github_search", "input": "string" },
    { "tool": "weather_fetch", "input": "string" }
  ]
}

If weather is not mentioned, exclude weather_fetch.
"""

def plan_task(user_task: str) -> dict:
    raw = ask_llm(SYSTEM_PROMPT, user_task)

    

    try:
        plan = json.loads(raw)
        return plan
    except json.JSONDecodeError:
        # 🛟 HARD FAILSAFE (never crash the system)
        return {
            "steps": [
                {"tool": "github_search", "input": user_task}
            ]
        }
