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
        print(f"Data root path: {self.default_root_path}")  # 调试信息
        os.makedirs(self.default_root_path, exist_ok=True)
        
        self.required_columns = [
            'tweet_id', 'text', 'event_id', 'words', 'filtered_words',
            'entities', 'user_id', 'created_at', 'urls', 'hashtags', 'user_mentions'
        ]
        self.repo_url = "https://gitee.com/kkunshao/social-ed_datasets.git"
        self.target_folder = "npy_data"

