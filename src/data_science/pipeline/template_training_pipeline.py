from abc import abstractmethod, ABC

class TemplateTrainingPipeline(ABC):
    @property
    @abstractmethod
    def stage(self):
        pass

    @abstractmethod
    def initiate(self):
        pass 
