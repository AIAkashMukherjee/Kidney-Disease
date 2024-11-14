import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.config.configuration import ConfigManager
from src.components.prepare_base_model import PrepareBaseModel
from src.logger.custom_logging import logger

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

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = BaseModelPipe()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e 