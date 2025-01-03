from src.inproject.config.configuration import ConfigurationManager
from src.inproject.component.model_trainer import ModelTrainer
# from mlproject.pipeline.stage_04_model_trainer import 
from src.inproject.logging import logger_re
from pathlib import Path

STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()



if __name__ == '__main__':
    try:
        logger_re.info(f'>>>stage {STAGE_NAME} started >>>>>')
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger_re.info(f'>>>>>>>>stage {STAGE_NAME} completed>>>>>>\n\nx===============')

    except Exception as e:
        logger_re.exception(e)
        raise e
