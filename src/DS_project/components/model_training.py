import pandas as pd
from src.DS_project.entity.config_entity import ModelTrainingConfig
from sklearn.linear_model import ElasticNet
import os
import joblib

class Model_Training:
    def __init__(self , config: ModelTrainingConfig):
        self.config = config

    def train_model(self):

        train_data = pd.read_csv(self.config.train_path)
        test_data = pd.read_csv(self.config.test_path)

        print(train_data.shape)


        train_x = train_data.drop(self.config.target_column , axis=1)
        train_y = train_data[self.config.target_column]
        test_x = test_data.drop(self.config.target_column , axis =1)
        test_y = test_data[self.config.target_column]

        print(f'Training data shape: {train_x.shape}')
        print(f'Training output shape: {train_y.shape}')

        lr = ElasticNet(alpha=self.config.alpha , l1_ratio=self.config.l1_ratio , random_state=42)

        lr.fit(train_x , train_y)

        joblib.dump(lr , os.path.join(self.config.root_dir , self.config.model_name))



        
