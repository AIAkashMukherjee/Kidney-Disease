import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_evalutaion.py',
    'src/components/model_trainer.py',
    'src/logger/custom_logging.py',
    'src/logger/__init__.py',
    'src/exceptions/expection.py',
    'src/exceptions/__init__.py',
    "src/utils/__init__.py",
    "src/utils/utlis.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipeline/__init__.py",
    'src/pipeline/training_pipeline.py',
    'src/pipeline/prediction_pipeline.py'
    "src/entity/__init__.py",
    "src/entity/config_entity.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    # for folder 
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")


    # for files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")