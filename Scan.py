import boto3

def scan_table(dynamo_client, *, TableName, **kwargs):

    paginator = dynamo_client.get_paginator("scan")

    for page in paginator.paginate(TableName=TableName, **kwargs):
        yield from page["Items"]


if __name__ == "__main__":
    dynamo_client = boto3.client("dynamodb")

    for item in scan_table(dynamo_client, TableName="TennisRacquets"):
        print(item)