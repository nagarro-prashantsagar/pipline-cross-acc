import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'update-lambda-code'
    key = 'lambda/my-code.zip'

    response = {
        'statusCode': 200,
        'body': json.dumps('Hello, This is Prashant sagar!,Hi their')
    }

    return response
