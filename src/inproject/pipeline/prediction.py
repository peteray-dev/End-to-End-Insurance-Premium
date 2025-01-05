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
        self.label_encoder = joblib.load(Path('artifacts/data_transformation/label_encoders.joblib'))
        

    def predict(self, data):
        """
        Preprocess the input data using saved transformers.
        """
        # Ensure the input is a DataFrame
        
        # if not isinstance(data, pd.DataFrame):
        #     data = pd.DataFrame(data)

        if 'Policy Start Date' in data.columns:
            data.drop(columns=['Policy Start Date'], inplace=True)

        
        # Identify categorical and numerical columns
        cat_cols = [col for col in data.columns if data[col].dtype == 'object']
        num_cols = [col for col in data.columns if data[col].dtype != 'object']

        print(f'categorical col{cat_cols}')
        print(f'numerical feat: {num_cols}')

        # Handle missing values
        data[num_cols] = self.num_imputer.transform(data[num_cols])
        data[cat_cols] = self.cat_imputer.transform(data[cat_cols])

        # print("LabelEncoder classes:", self.label_encoder.classes_)

        # Apply label encoding for categorical variables
        for col, encoder in self.label_encoder.items():
            print(f'column{col}, encoder{encoder}')
            data[col] = encoder.transform(data[col])
            
        print(f'data in predict after imputer{data}')
        # Scale numerical features
        data[num_cols] = self.scaler.transform(data[num_cols])
        # data[cat_cols] = self.scaler.transform(data[cat_cols])

        

        print(data)
        print(data.columns)
        predictions = self.model.predict(data)
        print(f'prediction result: {(predictions)}')
        return predictions

    # def predict(self, data):
    #     """
    #     Predict using the trained model.
    #     """
    #     # Preprocess the input data
    #     processed_data = self.preprocess_data(data)

    #     print(processed_data)
    #     # Predict using the loaded model
    #     predictions = self.model.predict(processed_data)

    #     return predictions
