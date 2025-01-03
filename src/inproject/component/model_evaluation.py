# import os
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
import numpy as np 
import joblib
from src.inproject.utils.common import save_json
from pathlib import Path
from src.inproject.config.configuration import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):
        rmse=np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, mae, r2
    
    def save_result(self):
    # Load test data and the trained model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        # Prepare test features and target
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Predictions and metrics for the test data
        predicted_test = model.predict(test_x)
        (rmse_test, mae_test, r2_test) = self.eval_metrics(test_y, predicted_test)

        # Load training data
        train_data = pd.read_csv(self.config.train_data_path)
        train_x = train_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]

        # Predictions and metrics for the training data
        predicted_train = model.predict(train_x)
        (rmse_train, mae_train, r2_train) = self.eval_metrics(train_y, predicted_train)

        # Save metrics for both training and testing
        scores = {
            'train': {'rmse': rmse_train, 'mae': mae_train, 'r2': r2_train},
            'test': {'rmse': rmse_test, 'mae': mae_test, 'r2': r2_test}
        }

        # Save the metrics to a JSON file
        save_json(path=Path(self.config.metric_file_name), data=scores)
