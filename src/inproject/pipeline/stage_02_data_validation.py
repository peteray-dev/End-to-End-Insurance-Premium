from src.inproject.config.configuration import ConfigurationManager
from src.inproject.component.data_validation import DataValidation
from src.inproject.logging import logger_re

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main():
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()
        data_validation.validate_datatypes()

        
if __name__ == '__main__':
    try:
        logger_re.info(f'>>>stage {STAGE_NAME} started >>>>>')
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger_re.info(f'>>>>>>>>stage {STAGE_NAME} completed>>>>>>\n\nx===============')

    except Exception as e:
        logger_re.exception(e)
        raise e