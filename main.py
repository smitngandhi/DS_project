from src.DS_project import logger
from src.DS_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DS_project.pipeline.data_validation_pipeline import DataValidationTrainingPipeline



STAGE_NAME_INGESTION = "Data_Ingestion_Pipeline"
STAGE_NAME_VALIDATION = "Data_Validation_Pipeline"
try:
    logger.info(f"{STAGE_NAME_INGESTION} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME_INGESTION} completed")

    logger.info("Starting Next Phase...")
    logger.info(f"{STAGE_NAME_VALIDATION} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_validation()
    logger.info(f"{STAGE_NAME_VALIDATION} completed")
except Exception as e:
    logger.exception(e)
    raise e

