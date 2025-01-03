import os
from pathlib import Path
import zipfile
import urllib.request as request
from src.inproject.logging import logger_re
from src.inproject.utils.common import read_yaml, get_size
from kaggle.api.kaggle_api_extended import KaggleApi
from src.inproject.entity.config_entity import DataIngestionCOnfig
# import kaggle



class DataIngestion:
    def __init__(self, config:DataIngestionCOnfig):
        self.config = config

   
    def download_data_from_kaggle(self):
        if not os.path.exists(self.config.local_data_file):
            os.makedirs(self.config.root_dir, exist_ok=True)
            api = KaggleApi()
            api.authenticate()
            api.competition_download_files(self.config.comp_name, self.config.root_dir)

            logger_re.info(f'data downloaded succesfully ')

        else:
            logger_re.info(f'file already exist of size: {get_size(Path(self.config.local_data_file))}')


    def extract_zip_file(self):
        """
        Extract the zip file into a directory and remove the zip file.
        Also removes all files except 'test.csv' after extraction.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        # Extract the zip file
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        # Delete the zip file
        os.remove(self.config.local_data_file)

        # Remove all files except 'test.csv' in the extracted directory
        for file in os.listdir(unzip_path):
            file_path = os.path.join(unzip_path, file)
            if file != 'train.csv' and os.path.isfile(file_path):
                os.remove(file_path)