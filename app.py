import json
from datetime import datetime

print('Loading function')


def lambda_handler(event, context):
    time_now = str(datetime.now())
    print(f'Received message at {time_now}')
    return f'Hello World {time_now}'

