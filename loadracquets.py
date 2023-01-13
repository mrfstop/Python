import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('TennisRacquets')

with open("racquetdata.json") as json_file:
    Racquets = json.load(json_file)
    for racquets in Racquets:
        brand = racquets['brand']
        model = racquets['model']
        
        print("Adding racquets:", brand, model)
        
        table.put_item(
           Item={
               'brand': brand,
               'model': model,
            }
        )