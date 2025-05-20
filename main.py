from agent.prompt_handler import parse_prompt
from agent.code_generator import generate_code
from agent.code_executor import execute_python_code

def run_agent(prompt: str):
    parsed = parse_prompt(prompt)
    code = generate_code(parsed["task"])
    print("Generated Code:\n", code)
    output = execute_python_code(code)
    print("\nExecution Output:\n", output)

if __name__ == "__main__":
    user_prompt = input("Enter your coding task: ")
    run_agent(user_prompt)
from agent.file_utils import save_code, log_execution_result

# Save generated code
file_path = save_code(code, filename_prefix="user_prompt")

# Log result
log_execution_result(code, output)
import yaml

with open("configs/agent.yaml", "r") as file:
    config = yaml.safe_load(file)

print("Agent:", config["agent"]["name"])
print("Supported Languages:", config["agent"]["supported_languages"])
