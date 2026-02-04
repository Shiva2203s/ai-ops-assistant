from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from agents.planner import plan_task
from agents.executor import execute_plan
from agents.verifier import verify_and_format

app = FastAPI()

@app.post("/run")
def run_task(task: str):
    plan = plan_task(task)
    results = execute_plan(plan)
    final_output = verify_and_format(results)
    return final_output
