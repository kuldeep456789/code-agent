import os
from datetime import datetime

# Ensure the directories exist
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CODE_DIR = os.path.join(BASE_DIR, "..", "generated_code")
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")

os.makedirs(CODE_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

def save_code(code: str, filename_prefix: str = "task") -> str:
    """
    Saves generated code to a Python file in the `generated_code` directory.
    Returns the path to the saved file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.py"
    filepath = os.path.join(CODE_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

    return filepath

def log_execution_result(code: str, output: str):
    """
    Logs the input code and the result/output to a central log file.
    """
    log_path = os.path.join(LOG_DIR, "execution_logs.txt")
    separator = "-" * 60
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"\n[{timestamp}] CODE GENERATED:\n")
        f.write(code + "\n")
        f.write(f"\nOUTPUT:\n{output}\n")
        f.write(f"{separator}\n")
