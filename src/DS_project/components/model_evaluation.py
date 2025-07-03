from sklearn.metrics import root_mean_squared_error , mean_absolute_error , r2_score
import mlflow
import pandas as pd
from urllib.parse import urlparse
from src.DS_project.config.configuration import ModelEvaluationConfig
import joblib
from src.DS_project import logger
from src.DS_project.utils.common import save_json
from pathlib import Path

class Model_evaluation:
    def __init__(self , config:ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual , predicted):
        rmse = root_mean_squared_error(actual , predicted)
        mae = mean_absolute_error(actual , predicted)
        r2 = r2_score(actual , predicted)

        return rmse , mae , r2
    
    def evaluate_with_mlflow(self):

        test = pd.read_csv(self.config.test_path)

        test_x = test.drop(self.config.target_column , axis = 1)
        test_y = test[self.config.target_column]

        model = joblib.load(self.config.model_path)
        logger.info("Model is loaded successfully")

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predictions = model.predict(test_x)

            logger.info("Predictions are ready")

            (rmse , mae , r2) = self.eval_metrics(test_y , predictions)

            scores = {'rmse': rmse , 'mae': mae , 'r2': r2}

            save_json(path=(Path(self.config.metrics_path)) , data=scores)

            mlflow.log_params(self.config.all_params)

            print("Tracking URI:", mlflow.get_tracking_uri())

            mlflow.log_metric('rmse' , rmse)
            mlflow.log_metric('mae', mae)
            mlflow.log_metric('r2' , r2)

            # mlflow.sklearn.log_model(sk_model=model)

            