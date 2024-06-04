import json
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Load the dataset configuration from dataset.json
with open('dataset.json', 'r') as f:
    config = json.load(f)

dataset = config.get('dataset')
path = config.get('path')
file_name = config.get('file_name')

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

# Download the dataset and unzip it
api.dataset_download_files(dataset, path=path, unzip=True)

# Load the dataset into a pandas DataFrame
data_path = f'{path}/{file_name}'
data = pd.read_csv(data_path)
