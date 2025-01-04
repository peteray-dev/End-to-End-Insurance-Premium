import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        self.scaler = joblib.load(Path('artifacts/data_transformation/scaler.joblib'))
        self.cat_imputer = joblib.load(Path('artifacts/data_transformation/cat_imputer.joblib'))
        self.num_imputer = joblib.load(Path('artifacts/data_transformation/num_imputer.joblib'))
        self.label_encoder = joblib.load(Path('artifacts/data_transformation/label_encoder.joblib'))
        

    def preprocess_data(self, data):
        """
        Preprocess the input data using saved transformers.
        """
        # Ensure the input is a DataFrame
        if not isinstance(data, pd.DataFrame):
            data = pd.DataFrame(data)

        data.drop(columns='Policy Start Date', inplace=True)
        # Identify categorical and numerical columns
        cat_cols = [col for col in data.columns if data[col].dtype == 'object']
        num_cols = [col for col in data.columns if data[col].dtype != 'object']

        print(data.columns)

        # Handle missing values
        data[num_cols] = self.num_imputer.transform(data[num_cols])
        data[cat_cols] = self.cat_imputer.transform(data[cat_cols])

        # Apply label encoding for categorical variables
        for col in cat_cols:
            data[col] = self.label_encoder.transform(data[col])

        # Scale numerical features
        data[num_cols] = self.scaler.transform(data[num_cols])

        return data

    def predict(self, data):
        """
        Predict using the trained model.
        """
        # Preprocess the input data
        processed_data = self.preprocess_data(data)

        # Predict using the loaded model
        predictions = self.model.predict(processed_data)

        return predictions
