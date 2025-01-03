from src.inproject.config.configuration import ConfigurationManager
from src.inproject.component.data_transformation import DataTransformation
from src.inproject.logging import logger_re

STAGE_NAME = "Data transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main():
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        train, test, cat_col, num_col = data_transformation.remove_outlier()
        train, test = data_transformation.replace_missing_values(train, test, cat_col, num_col)
        train, test = data_transformation.label_encoding_categorical(train, test, cat_col)
        data_transformation.scaling(train, test, num_col)

        
if __name__ == '__main__':
    try:
        logger_re.info(f'>>>stage {STAGE_NAME} started >>>>>')
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger_re.info(f'>>>>>>>>stage {STAGE_NAME} completed>>>>>>\n\nx===============')

    except Exception as e:
        logger_re.exception(e)
        raise e