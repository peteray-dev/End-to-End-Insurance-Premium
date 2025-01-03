import os
import pandas as pd
from src.inproject.logging import logger_re
from src.inproject.entity.config_entity import ModelTrainerConfig 
# from sklearn.linear_model import ElasticNet
from lightgbm import LGBMRegressor
import joblib

class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        lgbm = LGBMRegressor(n_estimators=self.config.n_estimators, learning_rate=self.config.learning_rate)
        lgbm.fit(train_x, train_y)

        joblib.dump(lgbm, os.path.join(self.config.root_dir, self.config.model_name))