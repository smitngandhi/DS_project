from src.DS_project import logger
from src.DS_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DS_project.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.DS_project.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.DS_project.pipeline.model_training_pipeline import ModelTrainingPipeline



STAGE_NAME_INGESTION = "Data_Ingestion_Pipeline"
STAGE_NAME_VALIDATION = "Data_Validation_Pipeline"
STAGE_NAME_TRANSFORMATION = "Data_Transformation_Pipeline"
STAGE_NAME_TRAINING = "Model_Training_Pipeline"
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


    logger.info("Starting Next Phase...")
    logger.info(f"{STAGE_NAME_TRANSFORMATION} started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_transformation()
    logger.info(f"{STAGE_NAME_TRANSFORMATION} completed")

    logger.info("Starting Next Phase...")
    logger.info(f"{STAGE_NAME_TRAINING} started")
    model_training = ModelTrainingPipeline()
    model_training.initiate_training()
    logger.info(f"{STAGE_NAME_TRAINING} completed")




except Exception as e:
    logger.exception(e)
    raise e

