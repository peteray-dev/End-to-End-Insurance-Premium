from src.inproject.constants import *
from src.inproject.utils.common import read_yaml, create_directories
from src.inproject.entity.config_entity import DataIngestionCOnfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig

# from inproject.entity.config_entity import
class ConfigurationManager:
    def __init__(self,
                 config_pathway = CONFIG_FILE_PATH,
                 param_pathway = PARAM_FILE_PATH,
                 schema_pathway = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_pathway)
        self.params = read_yaml(param_pathway)
        self.schema = read_yaml(schema_pathway)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionCOnfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionCOnfig(
            root_dir= config.root_dir,
            source_URL=config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir=config.unzip_dir,
            comp_name=config.comp_name
        )

        return data_ingestion_config
    
    def get_data_validation_config(self):
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema= schema
        )

        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transformation_config
    

    def get_model_trainer_config(self):
        config = self.config.model_trainer
        schema = self.schema.TARGET_COLUMN
        params = self.params.LGBMRegressor

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            n_estimators=params.n_estimators,
            learning_rate=params.learning_rate,
            target_column=schema.name
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
            config = self.config.model_evaluation
            params = self.params.LGBMRegressor
            schema = self.schema.TARGET_COLUMN

            create_directories([config.root_dir])

            data_evaluation_config = ModelEvaluationConfig(
                root_dir = config.root_dir,
                test_data_path=config.test_data_path,
                train_data_path=config.train_data_path,
                model_path=config.model_path,
                all_params=params,
                metric_file_name=config.metric_file_name,
                target_column=schema.name

            )

            return data_evaluation_config

    