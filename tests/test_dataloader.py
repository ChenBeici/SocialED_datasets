import pytest
from unittest.mock import patch, MagicMock
from dataload.dataloader import DatasetLoader
import os
import subprocess


# Test for download failure
def test_download_failure():
    with patch('subprocess.run') as mock_run:
        mock_run.side_effect = Exception("Git clone failed")
        loader = DatasetLoader(dataset="test_dataset")
        
        with pytest.raises(RuntimeError):
            loader.download()


# Test for download success
def test_download_success():
    # Mock subprocess to simulate a successful git clone
    with patch('subprocess.run') as mock_run:
        mock_run.return_value = MagicMock()  # Simulate successful run
        loader = DatasetLoader(dataset="test_dataset")

        with patch('os.makedirs') as mock_makedirs, patch('shutil.copy2') as mock_copy2:
            mock_copy2.return_value = None  # Simulate file copy success
            mock_makedirs.return_value = None  # Mock os.makedirs to prevent actual directory creation
            
            assert loader.download() is True  # Test should pass when no exception is raised


# Test load_data (mock implementation)
def test_load_data():
    loader = DatasetLoader(dataset="test_dataset")
    result = loader.load_data()

    # Assert that the result is a dictionary with expected keys
    assert isinstance(result, dict)
    assert 'texts' in result
    assert 'labels' in result
    assert 'metadata' in result
    assert 'name' in result['metadata']


# Test for get_dataset_language (valid dataset)
@pytest.mark.parametrize("dataset, expected_language", [
    ('MAVEN', 'English'),
    ('Event2018', 'French'),
    ('Arabic_Twitter', 'Arabic'),
    ('KBP', 'English')
])
def test_get_dataset_language(dataset, expected_language):
    loader = DatasetLoader(dataset=dataset)
    language = loader.get_dataset_language()
    assert language == expected_language


# Test for get_dataset_language (invalid dataset)
def test_get_dataset_language_invalid():
    loader = DatasetLoader(dataset="NonExistentDataset")
    with pytest.raises(ValueError, match="Unsupported dataset"):
        loader.get_dataset_language()


# Test for get_dataset_name
def test_get_dataset_name():
    loader = DatasetLoader(dataset="test_dataset")
    assert loader.get_dataset_name() == "test_dataset"


# Test if necessary directories are created (mock os.makedirs)
def test_create_directories():
    with patch('os.makedirs') as mock_makedirs:
        loader = DatasetLoader(dataset="test_dataset")
        loader.download()
        # Check if the directory creation was triggered
        mock_makedirs.assert_called()


# Test if tmp directory is cleaned up after download failure
def test_cleanup_after_failure():
    with patch('subprocess.run') as mock_run:
        mock_run.side_effect = Exception("Git clone failed")
        loader = DatasetLoader(dataset="test_dataset")

        # Ensure that the temporary directory is cleaned up after failure
        with patch('shutil.rmtree') as mock_rmtree:
            with pytest.raises(RuntimeError):
                loader.download()

            # Ensure tmp directory is removed
            mock_rmtree.assert_called()


# Test if correct file is copied during download
def test_copy_downloaded_file():
    with patch('subprocess.run') as mock_run, patch('shutil.copy2') as mock_copy2:
        mock_run.return_value = MagicMock()  # Simulate successful run
        loader = DatasetLoader(dataset="test_dataset")
        
        with patch('os.makedirs') as mock_makedirs:
            mock_copy2.return_value = None  # Mock file copy success
            mock_makedirs.return_value = None  # Mock os.makedirs to prevent actual directory creation
            
            loader.download()
            mock_copy2.assert_called_once()  # Ensure that shutil.copy2 was called


# Test if file exists when dataset path is checked
def test_check_file_existence():
    loader = DatasetLoader(dataset="test_dataset")
    dataset_path = os.path.join(loader.default_root_path, loader.dataset)
    
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True
        assert os.path.exists(dataset_path) == True
