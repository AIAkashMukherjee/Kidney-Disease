from src.config.configuration import ConfigManager
from src.components.model_evalutaion import Evaluation
from src.logger.custom_logging import logger
from src.exceptions.expection import CustomException
import sys


STAGE_NAME = "Model Evaluation stage"


class ModelEvalPipe:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigManager()
            eval_config = config.eval_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_with_mlflow()

        except Exception as e:
            raise CustomException(e,sys)