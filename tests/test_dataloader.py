import pytest
import os
import shutil
import numpy as np
import pandas as pd
from unittest.mock import patch, MagicMock
from  dataload.dataloader  import (
    DatasetLoader, MAVEN, CrisisNLP, Event2012, Event2018,
    ArabicTwitter, CrisisLexT26, CrisisMMD, HumAID, KBP
)

# Fixtures
@pytest.fixture
def temp_dir(tmp_path):
    """Create a temporary directory for testing"""
    return str(tmp_path)

@pytest.fixture
def mock_dataset():
    """Create mock dataset numpy array"""
    mock_data = np.array([
        [1, "text1", "event1", ["word1"], ["filtered1"], ["entity1"], 
         "user1", "2023-01-01", ["url1"], ["hashtag1"], ["mention1"]],
        [2, "text2", "event2", ["word2"], ["filtered2"], ["entity2"],
         "user2", "2023-01-02", ["url2"], ["hashtag2"], ["mention2"]]
    ], dtype=object)
    return mock_data

# Test DatasetLoader base class
class TestDatasetLoader:
    def test_init(self):
        loader = DatasetLoader(dataset="test_dataset", dir_path="/test/path")
        assert loader.dataset == "test_dataset"
        assert loader.dir_path == "/test/path"
        
    def test_get_dataset_language(self):
        # Test valid datasets
        loader = DatasetLoader(dataset="MAVEN")
        assert loader.get_dataset_language() == "English"
        
        loader = DatasetLoader(dataset="Event2018")
        assert loader.get_dataset_language() == "French"
        
        loader = DatasetLoader(dataset="Arabic_Twitter")
        assert loader.get_dataset_language() == "Arabic"
        
        # Test invalid dataset
        with pytest.raises(ValueError):
            DatasetLoader(dataset="InvalidDataset").get_dataset_language()
    
    def test_get_dataset_name(self):
        loader = DatasetLoader(dataset="MAVEN")
        assert loader.get_dataset_name() == "MAVEN"

    @patch('subprocess.run')
    def test_download_and_cleanup(self, mock_run, temp_dir, mock_dataset):
        loader = DatasetLoader(dataset="test_dataset")
        
        # Create mock repository structure
        repo_path = os.path.join(temp_dir, "repo")
        os.makedirs(repo_path)
        np.save(os.path.join(repo_path, "test_dataset.npy"), mock_dataset)
        
        # Mock successful git clone
        mock_run.return_value = MagicMock(returncode=0)
        
        result = loader.download_and_cleanup(
            "mock_url",
            "test_dataset",
            temp_dir
        )
        
        assert result == True
        mock_run.assert_called_once()

    def test_load_dataset(self):
        loader = DatasetLoader()
        data = loader.load_dataset()
        assert isinstance(data, dict)
        assert 'texts' in data
        assert 'labels' in data
        assert 'metadata' in data

# Test specific dataset classes
@pytest.mark.parametrize("dataset_class,dataset_name", [
    (MAVEN, "MAVEN"),
    (CrisisNLP, "CrisisNLP"),
    (Event2012, "Event2012"),
    (Event2018, "Event2018"),
    (ArabicTwitter, "Arabic_Twitter"),
    (CrisisLexT26, "CrisisLexT26"),
    (CrisisMMD, "CrisisMMD"),
    (HumAID, "HumAID"),
    (KBP, "KBP")
])
class TestDatasetClasses:
    def test_init(self, dataset_class, dataset_name):
        dataset = dataset_class()
        assert dataset.dataset == dataset_name
        
    def test_load_data_file_not_found(self, dataset_class, dataset_name, temp_dir):
        dataset = dataset_class(dir_path=temp_dir)
        dataset.load_data()
        assert os.path.exists(os.path.join(temp_dir, dataset_name)) == False

    @patch('SocialED_dataset.dataload.dataloader.DatasetLoader.download')
    def test_load_data_success(self, mock_download, dataset_class, dataset_name, 
                             temp_dir, mock_dataset):
        # Setup
        dataset = dataset_class(dir_path=temp_dir)
        dataset_path = os.path.join(dataset.default_root_path, dataset_name)
        os.makedirs(dataset_path, exist_ok=True)
        
        # Save mock data
        np.save(os.path.join(dataset_path, f"{dataset_name}.npy"), mock_dataset)
        
        # Test
        mock_download.return_value = True
        df = dataset.load_data()
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == len(mock_dataset)
        assert all(col in df.columns for col in dataset.required_columns)
        
        # Cleanup
        shutil.rmtree(dataset_path)

# Test error cases
def test_download_failure():
    with patch('subprocess.run') as mock_run:
        mock_run.side_effect = Exception("Git clone failed")
        loader = DatasetLoader(dataset="test_dataset")
        assert loader.download() == False

def test_invalid_dataset_path():
    loader = DatasetLoader(dataset="test_dataset", dir_path="/nonexistent/path")
    with pytest.raises(RuntimeError):
        loader.load_data()

if __name__ == "__main__":
    pytest.main(["-v", __file__])
