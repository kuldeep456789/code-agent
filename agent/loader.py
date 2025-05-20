# agent/config_loader.py
import yaml
import os

def load_config():
    path = os.path.join(os.path.dirname(__file__), "..", "configs", "agent_config.yaml")
    with open(path, "r") as file:
        return yaml.safe_load(file)
