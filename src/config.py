# src/config.py
import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()

def get_key():
    return os.getenv('API_KEY')

def get_data_dir():
    return os.getenv('DATA_DIR')