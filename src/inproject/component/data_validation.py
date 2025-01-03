import os
import pandas as pd
from src.inproject.logging import logger_re
from src.inproject.entity.config_entity import DataValidationConfig


# ~ Component

class DataValidation:
    def __init__(self, config=DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            validation_status=None
            data = pd.read_csv(self.config.unzip_data_dir)
            # print(data)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()
            # print(all_schema)
            # print(all_cols)

            for col in all_cols:
                if col not in all_schema:
                    validation_status=False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'validation status for columns is {validation_status}')

                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f'validation status for columns is {validation_status}')

                return validation_status
            
        except Exception as e:
            raise e
        
    def validate_datatypes(self)->bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_datatypes = list(data.dtypes)

            all_schema_datatypes = self.config.all_schema.values()

            for datatype in all_datatypes:
                
                if datatype not in all_schema_datatypes:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f'\nvalidation status for datatypes {validation_status}')
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f'\nvalidation status for datatype {validation_status}')

                return validation_status
            
        except Exception as e:
            raise e