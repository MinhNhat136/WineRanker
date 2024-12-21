from src.data_science.config.configuration import ConfigurationManager
from src.data_science.components.model_trainer import ModelTrainer
from src.data_science.pipeline.template_training_pipeline import TemplateTrainingPipeline

class ModelTrainerTrainingPipeline(TemplateTrainingPipeline):
    def __init__(self):
        pass

    def stage(self):
        return "Model Trainer stage"

    def initiate(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()