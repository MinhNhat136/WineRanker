import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import pandas as pd

sys.path.append("src")
from data_science.entity.config_entity import DataTransformationConfig
from data_science.components.data_transformation import DataTransformation

class TestDataTransformation(unittest.TestCase):

    def setUp(self):
        self.config = DataTransformationConfig(
            data_path="data_science/tests/mock_data/WineQT.csv",
            root_dir="data_science/tests/mock_data"
        )
        self.data_transformation = DataTransformation(config=self.config)

    @patch("data_science.components.data_transformation.pd.read_csv")
    @patch("data_science.components.data_transformation.train_test_split")
    @patch("data_science.components.data_transformation.os.path.join")
    @patch("data_science.components.data_transformation.pd.DataFrame.to_csv")
    @patch("data_science.logger.info")
    def test_train_test_splitting(self, mock_logger, mock_to_csv, mock_path_join, mock_train_test_split, mock_read_csv):
        # Mocking input data
        mock_data = pd.DataFrame({"feature": [1, 2, 3, 4], "label": [0, 1, 0, 1]})
        mock_read_csv.return_value = mock_data

        # Mocking train-test split
        train_data = mock_data.iloc[:2]
        test_data = mock_data.iloc[2:]
        mock_train_test_split.return_value = (train_data, test_data)

        # Mocking os.path.join
        mock_path_join.side_effect = lambda root, file: f"{root}/{file}"

        self.data_transformation.train_test_splitting()

        # Validating read_csv call
        mock_read_csv.assert_called_once_with(self.config.data_path)

        # Validating train_test_split call
        mock_train_test_split.assert_called_once_with(mock_data)

        # Validating to_csv calls
        mock_to_csv.assert_any_call("data_science/tests/mock_data/train.csv", index=False)
        mock_to_csv.assert_any_call("data_science/tests/mock_data/test.csv", index=False)

        # Validating logger calls
        mock_logger.assert_any_call("Splited data into training and test sets")
        mock_logger.assert_any_call(train_data.shape)
        mock_logger.assert_any_call(test_data.shape)

if __name__ == "__main__":
    unittest.main()
