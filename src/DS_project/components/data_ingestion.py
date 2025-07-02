import os
import urllib.request as request
from src.DS_project import logger
import zipfile
from src.DS_project.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self , config:DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.source_URL):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )

            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists")

    
    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path , exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)