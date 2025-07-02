from src.DS_project.constants import *
from src.DS_project.utils.common import *
from src.DS_project.entity.config_entity import (DataIngestionConfig , DataValidationConfig)

class ConfigurationManager:
    def __init__(self , 
                 config_path =CONFIG_FILE_PATH , 
                 params_path =PARAMS_FILE_PATH , 
                 schema_path=SCHEMA_FILE_PATH):
        self.config_path = read_yaml(config_path)
        self.params_path = read_yaml(params_path)
        self.schema_path = read_yaml(schema_path)

        create_directories([self.config_path.artifacts_root])

    def get_data_ingestion(self) -> DataIngestionConfig:
        config = self.config_path.data_ingestion
        create_directories([config.root_dir])

        data_ingestion = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion
    
    def get_data_validation(self) -> DataValidationConfig:
        config = self.config_path.data_validation
        schema = self.schema_path.COLUMNS
        create_directories([config.root_dir])

        data_validation = DataValidationConfig(
            root_dir = config.root_dir,
            unzip_data_dir= config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )

        return data_validation
