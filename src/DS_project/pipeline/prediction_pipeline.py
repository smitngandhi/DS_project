import joblib
from src.DS_project import logger

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load("artifacts/model_training/model.joblib")

    def predict(self , data):
        prediction = self.model.predict(data)

        logger.info("Predictions are ready")

        return prediction