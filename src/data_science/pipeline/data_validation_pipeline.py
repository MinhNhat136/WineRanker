from src.data_science.config.configuration import ConfigurationManager
from src.data_science.components.data_validation import DataValiadtion
from src.data_science import logger
from src.data_science.pipeline.template_training_pipeline import TemplateTrainingPipeline

class DataValidationTrainingPipeline(TemplateTrainingPipeline):
    def __init__(self):
        pass

    def stage(self):
        return "Data Validation stage"

    def initiate(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()

