from __future__ import print_function
import logging
import boto3
from datetime import *
from boto3.dynamodb.conditions import Key, Attr

# enable basic logging to CloudWatch Logs
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# setup the DynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('guinea-pig-temp')

# setup conversion to epoch
epoch = datetime.utcfromtimestamp(0)
now = datetime.now()


def lambda_handler(event, context):
    print ('event', event)

    table.put_item(
        Item={
                'device_id': event['source'],
                'published_at': int(unix_time_millis(datetime.strptime(event['published_at'], "%Y-%m-%dT%H:%M:%S.%fZ"))),
                'data': event['data']
        }
    )

    return("Success!")


# a function to convert the time to epoch
def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

