import pandas as pd
import os
import opendatasets as od
import json

DATASET_URL = "https://www.kaggle.com/competitions/nfl-big-data-bowl-2024/data"
DATA_PATH = ".." + os.sep
KAGGLE_PATH = "/root/.kaggle/kaggle.json"

api_token = {
    "username":"javiplaza",
    "key":"5786c1ce50f55d00309534407e8a71b4"
}

with open(KAGGLE_PATH, 'w') as file:
    json.dump(api_token, file)

od.download(DATASET_URL, data_dir=DATA_PATH)