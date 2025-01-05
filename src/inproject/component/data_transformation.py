from src.inproject.logging import logger_re
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from src.inproject.entity.config_entity import DataTransformationConfig
import os
import joblib


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def remove_outlier(self):
        data = pd.read_csv(self.config.data_path)
        data = data.drop(columns=['id','Policy Start Date'])
        train, test = train_test_split(data, test_size=0.20, random_state=42)

        cat_col = data.select_dtypes(include=['object']).columns.tolist()
        num_col = [col for col in train.select_dtypes(exclude=['object']).columns if col != 'Premium Amount']  # Exclude target
        # num_col = num_col[1:]
        print(f"Numerical Columns: {num_col}")
        print(f"Categorical Columns: {cat_col}")

        for col in num_col:
            Q1 = train[col].quantile(0.25)
            Q3 = train[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            train = train[(train[col] >= lower_bound) & (train[col] <= upper_bound)]

        print(f"Train shape after outlier removal: {train.shape}")
        print(f"Train shape after outlier removal: {train.columns}")
        print(f"Test shape after outlier removal: {test.shape}")

        return train, test, cat_col, num_col
    
    def replace_missing_values(self, train, test, cat_col, num_col):
        num_imputer = SimpleImputer(strategy='mean')
        cat_imputer = SimpleImputer(strategy='most_frequent')

        train[num_col] = num_imputer.fit_transform(train[num_col])
        test[num_col] = num_imputer.transform(test[num_col])

        train[cat_col] = cat_imputer.fit_transform(train[cat_col])
        test[cat_col] = cat_imputer.transform(test[cat_col])

        joblib.dump(num_imputer, os.path.join(self.config.root_dir, 'num_imputer.joblib'))
        joblib.dump(cat_imputer, os.path.join(self.config.root_dir, 'cat_imputer.joblib'))

        print(f"Train shape after missing value imputation: {train.shape}")
        print(f"Test shape after missing value imputation: {test.shape}")

        return train, test

    def label_encoding_categorical(self, train, test, cat_col):
        encoders = {}  # Dictionary to store LabelEncoders for each column

    # Iterate over each categorical column and apply LabelEncoder
        for col in cat_col:
            encoder = LabelEncoder()
            
            # Fit the encoder on the training data and transform both train and test
            train[col] = encoder.fit_transform(train[col])
            test[col] = encoder.transform(test[col])

            # Store the encoder in the dictionary
            encoders[col] = encoder

        # Save all encoders in a single joblib file
        joblib.dump(encoders, os.path.join(self.config.root_dir, 'label_encoders.joblib'))

        return train, test
    
    def scaling(self, train, test, num_col):
        scaler = StandardScaler()
        train[num_col] = scaler.fit_transform(train[num_col])
        test[num_col] = scaler.transform(test[num_col])
        
        joblib.dump(scaler, os.path.join(self.config.root_dir, 'scaler.joblib'))

        # Save the scaled train and test sets
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        # Logging
        logger_re.info("Split into training and test sets, with scaling applied.")
        logger_re.info(f"Train shape: {train.shape}")
        logger_re.info(f"Test shape: {test.shape}")

        print(f"Train shape after scaling: {train.shape}")
        print(f"Test shape after scaling: {test.shape}")