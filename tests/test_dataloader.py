import pytest
from unittest.mock import patch, MagicMock
from dataload.dataloader import DatasetLoader
import os

def test_download_success():
    """
    测试下载成功的情况
    模拟 git clone 成功并确保文件路径返回。
    """
    with patch('subprocess.run') as mock_run:
        # 模拟 git clone 成功
        mock_run.return_value = MagicMock()
        loader = DatasetLoader(dataset="test_dataset")
        
        # 模拟 os.makedirs 防止实际创建目录
        with patch('os.makedirs') as mock_makedirs:
            mock_makedirs.return_value = None  # Mock os.makedirs to prevent actual directory creation
            file_path = loader.download()
            
            # 确保文件路径返回并以 .npy 结尾
            assert file_path is not None
            assert file_path.endswith('test_dataset.npy')
            mock_makedirs.assert_called()

def test_download_failure():
    """
    测试下载失败的情况
    模拟 git clone 失败并确保抛出 RuntimeError。
    """
    with patch('subprocess.run') as mock_run:
        mock_run.side_effect = Exception("Git clone failed")
        loader = DatasetLoader(dataset="test_dataset")
        
        with pytest.raises(RuntimeError):
            loader.download()

def test_create_directories():
    """
    测试目标目录创建
    模拟 git clone 成功后，确保目标文件夹被创建。
    """
    with patch('subprocess.run') as mock_run:
        mock_run.return_value = MagicMock()  # Simulate successful run
        loader = DatasetLoader(dataset="test_dataset")
        
        with patch('os.makedirs') as mock_makedirs:
            mock_makedirs.return_value = None  # Mock os.makedirs to prevent actual directory creation
            loader.download()
            
            # Ensure the target folder is created
            mock_makedirs.assert_called()

def test_cleanup_after_failure():
    """
    测试在下载失败时，是否会清理已创建的临时目录
    模拟 git clone 失败并确保目标目录没有残留。
    """
    with patch('subprocess.run') as mock_run:
        mock_run.side_effect = Exception("Git clone failed")
        loader = DatasetLoader(dataset="test_dataset")
        
        # 模拟目标目录的创建
        local_target_folder = os.path.join(loader.default_root_path, loader.dataset)
        with patch('shutil.rmtree') as mock_rmtree:
            with pytest.raises(RuntimeError):
                loader.download()
            
            # 确保 rmtree 被调用
            mock_rmtree.assert_called_with(local_target_folder)

def test_copy_downloaded_file():
    """
    测试下载并复制文件的功能
    模拟文件成功下载，并确保文件被复制到目标目录。
    """
    with patch('subprocess.run') as mock_run, patch('shutil.copy2') as mock_copy2:
        mock_run.return_value = MagicMock()  # Simulate successful run
        loader = DatasetLoader(dataset="test_dataset")
        
        # 模拟文件复制成功
        mock_copy2.return_value = None
        with patch('os.makedirs') as mock_makedirs:
            mock_makedirs.return_value = None  # Mock os.makedirs to prevent actual directory creation
            file_path = loader.download()

            # 确保文件路径返回
            assert file_path is not None
            mock_copy2.assert_called()
            mock_makedirs.assert_called()

def test_invalid_dataset():
    """
    测试无效数据集的情况
    测试 `get_dataset_language` 是否抛出异常对于不支持的数据集。
    """
    loader = DatasetLoader(dataset="invalid_dataset")
    
    with pytest.raises(ValueError):
        loader.get_dataset_language()

def test_get_dataset_name():
    """
    测试获取数据集名称
    确保正确获取当前数据集的名称。
    """
    loader = DatasetLoader(dataset="test_dataset")
    dataset_name = loader.get_dataset_name()
    assert dataset_name == "test_dataset"

def test_get_dataset_language():
    """
    测试获取数据集语言
    确保返回正确的语言类型。
    """
    loader = DatasetLoader(dataset="MAVEN")
    language = loader.get_dataset_language()
    assert language == "English"
    
    loader = DatasetLoader(dataset="Event2018")
    language = loader.get_dataset_language()
    assert language == "French"
    
    loader = DatasetLoader(dataset="Arabic_Twitter")
    language = loader.get_dataset_language()
    assert language == "Arabic"

