from src.DS_project.components.model_evaluation import Model_evaluation
from src.DS_project.config.configuration import ConfigurationManager
import os
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/smitngandhi/DS_project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "smitngandhi"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "cead263a2fe84d23cdc7b91d33875c47d16c3e5b"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_evaluation(self):
        cm = ConfigurationManager()
        model_evaluation_config = cm.get_model_evaluation()
        model_evaluation = Model_evaluation(config=model_evaluation_config)
        model_evaluation.evaluate_with_mlflow()