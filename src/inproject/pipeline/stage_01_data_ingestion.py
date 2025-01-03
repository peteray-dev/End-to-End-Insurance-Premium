from src.inproject.config.configuration import ConfigurationManager
from src.inproject.component.data_ingestion import DataIngestion
from src.inproject.logging import logger_re

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main():
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data_from_kaggle()
        data_ingestion.extract_zip_file()

        
if __name__ == '__main__':
    try:
        logger_re.info(f'>>>stage {STAGE_NAME} started >>>>>')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger_re.info(f'>>>>>>>>stage one {STAGE_NAME} completed>>>>>>\n\nx===============')

    except Exception as e:
        logger_re.exception(e)
        raise e