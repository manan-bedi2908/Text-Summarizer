import os
import urllib
import zipfile
import requests
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
# from textSummarizer.config import DataIngestionConfig
from textSummarizer.entity import (DataIngestionConfig)
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urllib.request.urlretrieve(
                url = self.config.source_URL, 
                filename = self.config.local_data_file
            )
            # logger.info(f"Downloaded file: {filename} of size: {get_size(filename)}")
        else:
            # logger.info(f"File already exists: {self.config.local_data_file}")
            pass

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        