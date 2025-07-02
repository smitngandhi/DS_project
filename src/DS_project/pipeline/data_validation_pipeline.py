from src.DS_project.config.configuration import ConfigurationManager
from src.DS_project.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_validation(self):
        cm = ConfigurationManager()
        data_validation_config = cm.get_data_validation()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        
