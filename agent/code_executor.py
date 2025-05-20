import subprocess
import tempfile
import yaml

with open("configs/agent.yaml", "r") as file:
    config = yaml.safe_load(file)

TIMEOUT = config["execution"]["timeout"]

def execute_python_code(code: str) -> str:
    with tempfile.NamedTemporaryFile(mode='w+', suffix=".py", delete=False) as f:
        f.write(code)
        f.flush()
        try:
            output = subprocess.check_output(
                ["python", f.name],
                stderr=subprocess.STDOUT,
                timeout=TIMEOUT,
                text=True
            )
        except subprocess.CalledProcessError as e:
            output = f"Execution Error:\n{e.output}"
        except subprocess.TimeoutExpired:
            output = "Error: Code execution timed out."
    return output
