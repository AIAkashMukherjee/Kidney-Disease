from src.config.configuration import ConfigManager
from src.components.model_trainer import Training
from src.logger.custom_logging import logger
from src.exceptions.expection import CustomException
import sys


STAGE_NAME = "Model Training stage"


class ModelTrainPipe:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigManager()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
        except Exception as e:
            raise e        
