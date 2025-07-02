from src.DS_project import logger
from src.DS_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline



STAGE_NAME = "Data_Ingestion_Pipeline"
try:
    logger.info(f"{STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    raise e

