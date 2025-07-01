import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s')
project_name = "DS_project"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/config_entity.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "static/index.css"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath , "w") as f:
            logging.info(f'Creating empty file: {filepath}')
            pass

    else:
        logging.info(f"{filepath} already exists")

