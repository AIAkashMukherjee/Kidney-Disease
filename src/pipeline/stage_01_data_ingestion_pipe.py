import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.config.configuration import ConfigManager
from src.components.data_ingestion import DataIngestion
from src.logger.custom_logging import logger
from src.exceptions.expection import CustomException




STAGE_NAME = "Data Ingestion stage"


class DataIngestionPipe:
    def __init__(self):
        pass

    def main(self):
        try:
            config=ConfigManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipe()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e               