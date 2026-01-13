import logging
import os

def logging_function(prefix, timestamp):
    '''
    Sets up the logs
    
    :param prefix: For the folder name for the logs
    :param timestamp: For the name of the log files
    '''
    dir = f'{prefix}_logs'
    os.makedirs(dir, exist_ok=True)

    log_filename = f"{dir}/{timestamp}.log"

    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_filename
    )

    return logging.getLogger()


