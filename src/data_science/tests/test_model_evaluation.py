import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
import sys

sys.path.append("src")
from data_science.entity.config_entity import ModelEvaluationConfig
from data_science.components.model_evaluation import ModelEvaluation

class TestModelEvaluation(unittest.TestCase):

    def setUp(self):
        self.config = ModelEvaluationConfig(
            root_dir='data_science/tests/mock_data',
            test_data_path="data_science/tests/mock_data/WineQT.csv",
            model_path="/path/to/model.pkl",
            target_column="target",
            mlflow_uri="http://localhost:5000",
            metric_file_name="/path/to/metrics.json",
            all_params={"alpha": 0.5, "l1_ratio": 0.1}
        )
        self.model_evaluation = ModelEvaluation(config=self.config)

    def test_eval_metrics(self):
        actual = np.array([3.0, -0.5, 2.0, 7.0])
        pred = np.array([2.5, 0.0, 2.0, 8.0])
        rmse, mae, r2 = self.model_evaluation.eval_metrics(actual, pred)

        self.assertAlmostEqual(rmse, 0.6123724356957945)
        self.assertAlmostEqual(mae, 0.5)
        self.assertAlmostEqual(r2, 0.9486081370449679)

    @patch("data_science.components.model_evaluation.mlflow.start_run")
    @patch("data_science.components.model_evaluation.mlflow.sklearn.log_model")
    @patch("data_science.components.model_evaluation.mlflow.log_metric")
    @patch("data_science.components.model_evaluation.mlflow.log_params")
    @patch("data_science.components.model_evaluation.joblib.load")
    @patch("data_science.components.model_evaluation.pd.read_csv")
    @patch("data_science.components.model_evaluation.save_json")
    def test_log_into_mlflow(self, mock_save_json, mock_read_csv, mock_load_model,
                             mock_log_params, mock_log_metric, mock_log_model, mock_start_run):
        # Mocking test data
        mock_test_data = pd.DataFrame({"feature": [1, 2, 3, 4], "target": [0.5, 1.5, 3.5, 4.5]})
        mock_read_csv.return_value = mock_test_data

        # Mocking model
        mock_model = MagicMock()
        mock_model.predict.return_value = [0.5, 1.5, 3.5, 4.5]
        mock_load_model.return_value = mock_model

        self.model_evaluation.log_into_mlflow()

        # Assertions for method calls
        mock_read_csv.assert_called_once_with(self.config.test_data_path)
        mock_load_model.assert_called_once_with(self.config.model_path)
        mock_log_params.assert_called_once_with(self.config.all_params)
        mock_log_metric.assert_any_call("rmse", 0.0)
        mock_log_metric.assert_any_call("r2", 1.0)
        mock_log_metric.assert_any_call("mae", 0.0)
        mock_save_json.assert_called_once()

if __name__ == "__main__":
    unittest.main()
