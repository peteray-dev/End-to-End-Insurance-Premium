from src.inproject.logging import logger_re
from src.inproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.inproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.inproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.inproject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.inproject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger_re.info(f'>>>>>>>{STAGE_NAME} started>>>>>>>>')
    data_ingestion = DataIngestionTrainingPipeline
    data_ingestion.main()
    logger_re.info(f'>>>>>>stage {STAGE_NAME} completed >>>>>>>')

except Exception as e:
    logger_re.exception(e)
    raise e

STAGE_NAME = 'Data Validation Stage'

try:
    logger_re.info(f'>>>>>>>{STAGE_NAME} started>>>>>>>>')
    data_ingestion = DataValidationTrainingPipeline
    data_ingestion.main()
    logger_re.info(f'>>>>>>stage {STAGE_NAME} completed >>>>>>>')

except Exception as e:
    logger_re.exception(e)
    raise e


STAGE_NAME = 'Data transformation Stage'

try:
    logger_re.info(f'>>>>>>>{STAGE_NAME} started>>>>>>>>')
    data_ingestion = DataTransformationTrainingPipeline
    data_ingestion.main()
    logger_re.info(f'>>>>>>stage {STAGE_NAME} completed >>>>>>>')

except Exception as e:
    logger_re.exception(e)
    raise e

STAGE_NAME = 'Model Trainer Stage'

try:
    logger_re.info(f'>>>>>>>{STAGE_NAME} started>>>>>>>>')
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.main()
    logger_re.info(f'>>>>>>stage {STAGE_NAME} completed >>>>>>>')

except Exception as e:
    logger_re.exception(e)
    raise e

STAGE_NAME = 'Model Evaluation Stage'

try:
    logger_re.info(f'>>>>>>>{STAGE_NAME} started>>>>>>>>')
    data_evaluation = ModelEvaluationPipeline()
    data_evaluation.main()
    logger_re.info(f'>>>>>>stage {STAGE_NAME} completed >>>>>>>')

except Exception as e:
    logger_re.exception(e)
    raise e


