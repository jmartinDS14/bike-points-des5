import boto3
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
bucket_name=os.getenv('bucket_name')

data_dir = Path('data')
json_files = list(data_dir.glob('*.json'))

s3_client = boto3.client(
    's3'
    ,aws_access_key_id = AWS_ACCESS_KEY
    ,aws_secret_access_key = AWS_SECRET_KEY
)
if len(json_files)>0:
    for file in json_files:
        s3_filename = os.path.basename(file)
        try:
            s3_client.upload_file(file,bucket_name,s3_filename)
            os.remove(file)
        except Exception as e:
            print(e)
else:
    print('No files :(')
    