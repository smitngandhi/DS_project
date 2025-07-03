from src.DS_project.entity.config_entity import DataTransformationConfig
import pandas as pd
from src.DS_project import logger
import os
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self , config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train , test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir , 'train.csv'))
        test.to_csv(os.path.join(self.config.root_dir , "test.csv"))


        logger.info("Train and Test data arre saved ")

        print(train.shape)
        print(test.shape)

