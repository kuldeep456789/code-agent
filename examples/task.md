## Main Files
main.py
This is the main file. It reads what you type, asks the AI to write code, then runs that code and shows you the result.

requirements.txt
This file lists all the Python tools (libraries) the project needs to work. You can install them using:

bash
Copy
Edit
pip install -r requirements.txt
agent/ Folder – Core Functions

## agent dir
code_generator.py – Uses AI (like ChatGPT) to turn your text into Python code.

code_executor.py – Runs the code safely and stops it if it takes too long.

prompt_handler.py – Helps the AI better understand what you’re asking.

file_utils.py – Saves files and logs. It helps manage reading and writing to the disk.

loader.py – Loads settings or files when needed.

__pycache__/ – Automatically created by Python to make things run faster. You can ignore it.




## configs/ Folder – Settings
agent.yaml
This file controls how the AI behaves (like which model to use, how creative it is, and how long it should wait for code to finish running).


## examples/ Folder
task.md
This file (what you’re reading) explains how the project is organized.


## logs/ Folder
logs.txt
This keeps a record of all code that has been created and run, along with the results. Helpful for tracking what the agent has done.
