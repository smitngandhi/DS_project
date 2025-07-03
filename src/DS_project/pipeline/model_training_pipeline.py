from src.DS_project.config.configuration import ConfigurationManager
from src.DS_project.components.model_training import Model_Training

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_training(self):
        cm = ConfigurationManager()
        model_training_config = cm.get_model_training()
        model_training = Model_Training(config=model_training_config)
        model_training.train_model()