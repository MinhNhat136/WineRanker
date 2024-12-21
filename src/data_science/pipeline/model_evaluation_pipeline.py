from src.data_science.config.configuration import ConfigurationManager
from src.data_science.components.model_evaluation import ModelEvaluation
from src.data_science.pipeline.template_training_pipeline import TemplateTrainingPipeline

class ModelEvaluationTrainingPipeline(TemplateTrainingPipeline):
    def __init__(self):
        pass

    def stage(self):
        return "Model evaluation stage"

    def initiate(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()