from src.config.configuration import ConfigManager
from src.components.prepare_base_model import PrepareBaseModel
from src.logger.custom_logging import logger
from src.exceptions.expection import CustomException
import sys


STAGE_NAME = "Prepare Base Model stage"


class BaseModelPipe:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigManager()
            prepare_base_model_config = config.prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e        
