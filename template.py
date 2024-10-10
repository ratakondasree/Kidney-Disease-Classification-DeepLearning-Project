
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name='cnnClassifier'

list_of_files=[
".github/workflows/.gitkeep",
f"src/{project_name}/__init__.py",
f"src/{project_name}/components/__init__.py",
f"src/{project_name}/utils/__init__.py",
f"src/{project_name}/config/__init__.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/entity/__init__.py",
f"src/{project_name}/pipeline/__init__.py",
f"config/config.yaml",
f"dvc.yaml",
f"params.yaml",
f"requirements.txt",
f"research/trails.ipynb",
f"research/trails.ipynb",
f"templates/index.html"


]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)


    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory : {filedir} for the filename :{filename}")
    

    if (not os.path.exists(filepath))  or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file : {filename}")
    else:
        logging.info(f"{filename} is already exists")