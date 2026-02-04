title: "AI Operations Assistant – GenAI Intern Assignment"

objective: >
  Build an AI Operations Assistant that accepts a natural-language task,
  plans execution steps using an LLM, executes those steps via real APIs,
  verifies results, and returns a structured end-to-end response.

architecture_overview:
  description: "Multi-agent architecture with clear separation of responsibilities"
  agents:
    planner:
      responsibilities:
        - Convert user input into structured JSON execution plan
        - Use LLM for reasoning
        - Select tools to be used
        - Does not execute APIs
    executor:
      responsibilities:
        - Execute steps defined by Planner
        - Call real third-party APIs via tools
        - Does not perform reasoning or validation
    verifier:
      responsibilities:
        - Validate executor results
        - Ensure required fields are present
        - Apply graceful fallback when partial data is unavailable
        - Produce final structured response

integrated_apis:
  - name: "Groq LLM API"
    model: "LLaMA-3.1-8B-Instant"
    purpose: "Planning and reasoning"
  - name: "GitHub Search API"
    purpose: "Fetch popular repositories"
  - name: "OpenWeather API"
    purpose: "Fetch weather data (optional, graceful fallback supported)"

project_structure: |
  ai_ops_assistant/
  ├── agents/
  │   ├── planner.py
  │   ├── executor.py
  │   └── verifier.py
  ├── tools/
  │   ├── github_tool.py
  │   └── weather_tool.py
  ├── llm/
  │   └── client.py
  ├── main.py
  ├── requirements.txt
  ├── .env.example
  └── README.md

setup_instructions:
  step_1:
    description: "Clone the repository"
    commands:
      - "git clone <your-repo-url>"
      - "cd ai_ops_assistant"
  step_2:
    description: "Create and activate Conda environment"
    commands:
      - "conda create -n ai_ops python=3.10"
      - "conda activate ai_ops"
  step_3:
    description: "Install dependencies"
    commands:
      - "pip install -r requirements.txt"
  step_4:
    description: "Configure environment variables"
    env_file: ".env"
    variables:
      GROQ_API_KEY: "your_groq_api_key_here"
      OPENWEATHER_API_KEY: "your_openweather_api_key_here"
    note: "Refer to .env.example for required variables"

running_the_project:
  command: "uvicorn main:app"
  swagger_url: "http://127.0.0.1:8000/docs"

example_prompts:
  - "Find 3 popular Python GitHub repositories"
  - "Get the weather in Pune"
  - "Find popular JavaScript repositories and the weather in Mumbai"
  - "Search top machine learning GitHub repositories"
  - "Find system design related GitHub repositories"

known_limitations_tradeoffs:
  - "Weather data gracefully degrades when the OpenWeather API key is missing or invalid"
  - "Planner output depends on LLM response quality"
  - "GitHub API unauthenticated requests are rate-limited"
  - "No caching or parallel execution implemented"
