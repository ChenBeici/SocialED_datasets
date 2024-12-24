import unittest
import os
import shutil
import tempfile
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataload.dataloader import DatasetLoader

class TestDatasetLoader(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.loader = DatasetLoader(dir_path=self.test_dir)

    def tearDown(self):
        # Clean up the temporary directory after tests
        shutil.rmtree(self.test_dir)

    def test_init(self):
        # Test initialization
        self.assertEqual(self.loader.dir_path, self.test_dir)
        self.assertIsNone(self.loader.dataset)
        self.assertTrue(os.path.exists(self.loader.default_root_path))
        
        # Test required columns
        expected_columns = [
            'tweet_id', 'text', 'event_id', 'words', 'filtered_words',
            'entities', 'user_id', 'created_at', 'urls', 'hashtags', 'user_mentions'
        ]
        self.assertEqual(self.loader.required_columns, expected_columns)
        
        # Test repo URL and target folder
        self.assertEqual(self.loader.repo_url, "https://gitee.com/kkunshao/social-ed_datasets.git")
        self.assertEqual(self.loader.target_folder, "npy_data")

if __name__ == '__main__':
    unittest.main()
