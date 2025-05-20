from langchain_openai import ChatOpenAI
import yaml

with open("configs/agent.yaml", "r") as file:
    config = yaml.safe_load(file)

llm = ChatOpenAI(
    model=config["model"]["model_name"],
    temperature=config["model"]["temperature"],
    openai_api_key="AIzaSyCnww2uoPSvA6nNz9PkZ4pYn8px31PlmCA"
)

def generate_code(task: str) -> str:
    from langchain.prompts import ChatPromptTemplate
    prompt = ChatPromptTemplate.from_template("Write Python code to: {task}")
    chain = prompt | llm
    return chain.invoke({"task": task}).content.strip()
