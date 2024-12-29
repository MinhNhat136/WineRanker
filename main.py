from src.data_science import logger
from src.data_science.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.data_science.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.data_science.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.data_science.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.data_science.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline
from src.data_science.pipeline.template_training_pipeline import TemplateTrainingPipeline

def execute_stage(stage: TemplateTrainingPipeline):
   try:
      logger.info(f">>>>>> stage {stage.stage} started <<<<<<") 
      stage.initiate()
      logger.info(f">>>>>> stage {stage.stage} completed <<<<<<\n\nx==========x")
   except Exception as e:
      logger.exception(e)
      raise e

data_ingestion = DataIngestionTrainingPipeline()
data_validation = DataValidationTrainingPipeline()
data_transformation = DataTransformationTrainingPipeline()
model_trainer = ModelTrainerTrainingPipeline()
model_evaluation = ModelEvaluationTrainingPipeline()

pipeline = [data_ingestion, data_validation, data_transformation, 
            model_trainer, model_evaluation]

for stage in pipeline:
   execute_stage(stage)

   