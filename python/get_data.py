from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from datetime import *
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

epoch = datetime.utcfromtimestamp(0)

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
        
def int_to_date(as_int):
    #t = timedelta(0,seconds=float(as_int)/1000.0)
    t = timedelta(0,seconds=as_int/1000)
    return epoch + t
    
def pretty_print_date(dt):
    return datetime.strftime(dt, "%Y-%m-%dT%H:%M:%S.%fZ")

dynamodb = boto3.resource("dynamodb", region_name='us-west-2')

table = dynamodb.Table('guinea-pig-temp')

try:
    response = table.query(KeyConditionExpression=Key('device_id').eq('3b0040001647343339383037'))
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    for i in response['Items']:
        print (pretty_print_date(int_to_date(int(i['published_at']))))
        print (dict(item.split("=") for item in i['data'].split(",").strip()))
#        print(json.dumps(i, indent=4, cls=DecimalEncoder))
#        o = json.load(i)
#        print (o)