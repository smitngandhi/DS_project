from src.DS_project.config.configuration import ConfigurationManager
from src.DS_project.components.data_ingestion import DataIngestion
STAGE_NAME = "Data_ingestion_pipeline"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        cm = ConfigurationManager()
        data_ingestion_config= cm.get_data_ingestion()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip()

