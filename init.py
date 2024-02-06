import json
import os
import tkinter as tk
from tkinter import simpledialog
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import subprocess


def get_credentials_and_create_kaggle_json():
    # Use Tkinter to get credentials from user
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    username = simpledialog.askstring("Kaggle Username", "Enter your Kaggle username:", parent=root)
    key = simpledialog.askstring("Kaggle Key", "Enter your Kaggle API key:", parent=root, show='*')
    root.destroy()

    # Create .kaggle directory in user's home directory if it doesn't exist
    kaggle_dir = os.path.expanduser('~/.kaggle')
    os.makedirs(kaggle_dir, exist_ok=True)

    # Path for kaggle.json
    kaggle_json_path = os.path.join(kaggle_dir, 'kaggle.json')

    # Save credentials to kaggle.json
    with open(kaggle_json_path, 'w') as json_file:
        json.dump({"username": username, "key": key}, json_file)

    print(f'Kaggle API credentials file created at {kaggle_json_path}')


def download_and_unzip_data(competition_name, download_path):
    # Ensure download path exists
    os.makedirs(download_path, exist_ok=True)

    # Authenticate with Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Download data
    print('Downloading data...')
    api.competition_download_files(competition_name, download_path)

    # Find downloaded zip file
    zip_file_path = os.path.join(download_path, f'{competition_name}.zip')

    # Unzip data
    print('Unzipping data...')
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(download_path)

    # Clean up zip file
    os.remove(zip_file_path)
    print('Data downloaded and extracted successfully.')


get_credentials_and_create_kaggle_json()
download_and_unzip_data('nfl-big-data-bowl-2024', 'dataset')
subprocess.run(["docker", "compose", "up", "-d"])


