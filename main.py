from modules.logging import logging_function
from modules.extract import extract_function
from modules.load import load_function
from datetime import datetime
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
bucket_name=os.getenv('bucket_name')

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
url = 'https://api.tfl.gov.uk/BikePoint'

extract_logger = logging_function('extract',timestamp)

extract_function(url, 3, extract_logger, timestamp)

load_logger = logging_function('load',timestamp)

load_function(Path('data'),AWS_ACCESS_KEY,AWS_SECRET_KEY,bucket_name,load_logger)