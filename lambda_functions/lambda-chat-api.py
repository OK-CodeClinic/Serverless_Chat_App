import json
import boto3

s3_client = boto3.client('s3')

bucket_name = 'ken-serverless-chat-application'

def lambda_handler(event, context):
    try:
        # Retrieve the object from S3
        response = s3_client.get_object(Bucket=bucket_name, Key='data/conversations.json')
        
        # Read the response body (assuming it's JSON) and parse it
        response_body = response['Body'].read().decode('utf-8')
        parsed_response = json.loads(response_body)
        
        return {
            'statusCode': 200,
            'body': json.dumps(parsed_response),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 400,
            'body': json.dumps(str(e)),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
