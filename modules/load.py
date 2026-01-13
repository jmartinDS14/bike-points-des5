import boto3
import os

def load_function(data_dir, AWS_ACCESS_KEY, AWS_SECRET_KEY, bucket_name, logger):
    '''
    Loads json data from data_dir to S3 bucket.
    
    :param data_dir: Description
    :param access_key: Description
    :param secret_access_key: Description
    :param bucket: Description
    :param logger: Description
    '''
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
                logger.info(f'{file} uploaded successfully')
            except Exception as e:
                print(e)
                logger.error(f'{e}')
    else:
        print('No files :(')
        logger.warning('No files :(')