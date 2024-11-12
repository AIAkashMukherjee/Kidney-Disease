from src.logger.custom_logging import logger
from src.pipeline.stage_01_data_ingestion_pipe import DataIngestionPipe
from src.pipeline.stage_02_prepare_base_model import BaseModelPipe
from src.pipeline.stage_03_model_Trainer import ModelTrainPipe
from src.exceptions.expection import CustomException
import sys

# STAGE_NAME = "Data Ingestion stage"
# try:
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#    data_ingestion = DataIngestionPipe()
#    data_ingestion.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e



def run_stage(stage_name, pipeline_class):
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        pipeline = pipeline_class()
        pipeline.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)
    
if __name__ == "__main__":
    stages = [
        ("Data Ingestion stage", DataIngestionPipe),
        ("Base Model stage", BaseModelPipe),
      #   ("Data Transformation stage", DataTransformationTrainingPipeline),
        ("Model Trainer stage", ModelTrainPipe),
      #   ("Model Evaluation stage", ModelEvalPipeline),
    ]

    for stage_name, pipeline_class in stages:
        run_stage(stage_name, pipeline_class)    