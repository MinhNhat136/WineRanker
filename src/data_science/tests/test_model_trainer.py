import unittest
import sys
from unittest.mock import patch, MagicMock
import pandas as pd

sys.path.append("src")
from data_science.entity.config_entity import ModelTrainerConfig
from data_science.components.model_trainer import ModelTrainer

class TestModelTrainer(unittest.TestCase):

    def setUp(self):
        self.config = ModelTrainerConfig(
            train_data_path="/path/to/train.csv",
            test_data_path="/path/to/test.csv",
            target_column="target",
            root_dir="/path/to/root",
            model_name="model.pkl",
            alpha=0.5,
            l1_ratio=0.1
        )
        self.model_trainer = ModelTrainer(config=self.config)

    @patch("data_science.components.model_trainer.pd.read_csv")
    @patch("data_science.components.model_trainer.joblib.dump")
    def test_train(self, mock_dump, mock_read_csv):
        # Mocking train and test data
        mock_train_data = pd.DataFrame({"feature": [1, 2, 3, 4], "target": [0.5, 1.5, 3.5, 4.5]})
        mock_read_csv.side_effect = [mock_train_data, mock_train_data]

        self.model_trainer.train()

        # Assertions for read_csv and dump calls
        mock_read_csv.assert_any_call(self.config.train_data_path)
        mock_read_csv.assert_any_call(self.config.test_data_path)
        mock_dump.assert_called_once()

if __name__ == "__main__":
    unittest.main()
