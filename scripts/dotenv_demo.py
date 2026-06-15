from dotenv import load_dotenv
import os
from my_cool_package.logger.setup_logger import setup_logger

# Set up the logger
logger = setup_logger()
logger.info("Starting the dotenv demo script.")

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
root_path = os.getenv("ROOT")
shared_storage = os.getenv("SHARED_STORAGE")
external_data = os.getenv("EXTERNAL_DATA")
local_data = os.getenv("LOCAL_DATA")
dataset = os.getenv("DATASET")

# Log the loaded environment variables
logger.info(f"ROOT: {root_path}")
logger.info(f"SHARED_STORAGE: {shared_storage}")
logger.info(f"EXTERNAL_DATA: {external_data}")
logger.info(f"LOCAL_DATA: {local_data}")
logger.info(f"DATASET: {dataset}")
