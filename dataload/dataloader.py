import numpy as np
import os
from git import Repo, GitCommandError
import pandas as pd
import shutil
from uuid import uuid4
from datetime import datetime
import subprocess
import tempfile

class DatasetLoader:
    def __init__(self, dataset=None, dir_path=None):
        self.dir_path = dir_path
        self.dataset = dataset
        self.default_root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../dataset/data"))
        #print(f"Data root path: {self.default_root_path}")  # 调试信息
        os.makedirs(self.default_root_path, exist_ok=True)
        
        self.required_columns = [
            'tweet_id', 'text', 'event_id', 'words', 'filtered_words',
            'entities', 'user_id', 'created_at', 'urls', 'hashtags', 'user_mentions'
        ]
        self.repo_url = "https://github.com/ChenBeici/SocialED_datasets.git"
        self.target_folder = "npy_data"

    def download_and_cleanup(self, repo_url, dataset_name, local_target_folder):
        try:
            print(f"Downloading {dataset_name}.npy from {repo_url}")
            
            # 直接将仓库克隆到目标文件夹
            subprocess.run(['git', 'clone', '--branch', 'main', repo_url, local_target_folder], check=True)
            
            # 确保目标目录存在
            os.makedirs(local_target_folder, exist_ok=True)
            print(f"Target directory: {local_target_folder}")
            
            # 搜索 .npy 文件
            npy_files = []
            for root, dirs, files in os.walk(local_target_folder):
                for file in files:
                    if file == f'{dataset_name}.npy':
                        npy_files.append(os.path.join(root, file))
            
            if npy_files:
                target_file = npy_files[0]  # 使用下载后的文件
                print(f"Using downloaded file: {target_file}")
                return target_file
            else:
                print(f"Error: {dataset_name}.npy not found in repository")
                return None

        except Exception as e:
            print(f"Error during download: {str(e)}")
            return None

    def download(self):
        local_target_folder = os.path.join(self.default_root_path, self.dataset)
        file_path = self.download_and_cleanup(self.repo_url, self.dataset, local_target_folder)
        if not file_path:
            raise RuntimeError(f"Failed to download {self.dataset} dataset.")
        return file_path

    def load_data(self):
        """Temporary implementation that returns empty dataset"""
        print(f"Loading {self.dataset} dataset (mock data)")
        return {
            'texts': [],
            'labels': [],
            'metadata': {'name': self.dataset}
        }

    def get_dataset_language(self):
        """
        Determine the language based on the current dataset.
        
        Returns:
            str: The language of the dataset ('English', 'French', 'Arabic').
        """
        dataset_language_map = {
            'MAVEN': 'English',
            'Event2012': 'English', 
            'Event2018': 'French',
            'Arabic_Twitter': 'Arabic',
            'CrisisLexT26': 'English',
            'CrisisLexT6': 'English', 
            'CrisisMMD': 'English',
            'CrisisNLP': 'English',
            'HumAID': 'English',
            'ICWSM2018': 'English',
            'ISCRAM2013': 'English',
            'BigCrisisData': 'English',
            'KBP': 'English',
            'Event2012_100': 'English',
            'Event2018_100': 'French',
            'Arabic_100': 'Arabic'
        }
        
        language = dataset_language_map.get(self.dataset)
        if not language:
            raise ValueError(f"Unsupported dataset: {self.dataset}. Supported datasets are: {', '.join(dataset_language_map.keys())}")
        return language

    def get_dataset_name(self):
        """
        Get the name of the current dataset.
        
        Returns:
            str: The name of the dataset.
        """
        return self.dataset
