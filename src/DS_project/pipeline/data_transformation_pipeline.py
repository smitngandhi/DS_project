from src.DS_project.config.configuration import ConfigurationManager
from src.DS_project.components.data_transformation import DataTransformation
from src.DS_project import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_transformation(self):
        try:
            with open("artifacts/data_validation/status.txt" , "r") as f:
                status = f.read().split(" ")[-1]
            if status=="True":
                cm = ConfigurationManager()
                data_transformation_config = cm.get_data_transformation()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data is not valid")
            
        except Exception as e:
            logger.exception(e)
            raise e