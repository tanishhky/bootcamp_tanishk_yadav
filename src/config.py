import os
from dotenv import load_dotenv

def load_env():
    """Loads environment variables from .env file."""
    load_dotenv()

def get_key(key_name="API_KEY"):
    """Fetches a specific key from the environment variables."""
    return os.getenv(key_name)

# Load environment variables on import
load_env()
DATA_DIR_RAW = os.getenv("DATA_DIR_RAW", "data/raw")
DATA_DIR_PROCESSED = os.getenv("DATA_DIR_PROCESSED", "data/processed")