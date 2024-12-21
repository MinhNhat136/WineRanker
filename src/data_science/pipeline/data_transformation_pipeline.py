from src.data_science.config.configuration import ConfigurationManager
from src.data_science.components.data_transformation import DataTransformation
from src.data_science import logger
from src.data_science.pipeline.template_training_pipeline import TemplateTrainingPipeline
from pathlib import Path


class DataTransformationTrainingPipeline(TemplateTrainingPipeline):
    def __init__(self):
        pass

    def stage(self):
        return "Data Transformation Stage"

    def initiate(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data scheme is not valid")
            
        except Exception as e:
            print(e)