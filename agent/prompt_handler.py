def parse_prompt(prompt: str) -> dict:
    # Example: extract language, task, and constraints
    return {
        "language": "python",
        "task": prompt.strip()
    }
