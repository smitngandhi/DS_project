from src.DS_project.components.model_evaluation import Model_evaluation
from src.DS_project.config.configuration import ConfigurationManager
import os
from dotenv import load_dotenv

load_dotenv()


os.environ["MLFLOW_TRACKING_URI"] = os.getenv("MLFLOW_TRACKING_URI")
os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME")
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_evaluation(self):
        cm = ConfigurationManager()
        model_evaluation_config = cm.get_model_evaluation()
        model_evaluation = Model_evaluation(config=model_evaluation_config)
        model_evaluation.evaluate_with_mlflow()