import json
import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# Define the S3 bucket name
bucket = 'ken-serverless-chat-application'

def lambda_handler(event, context):
    # Extract the path from the event
    path = event['pathParameters']['proxy']

    key = None

    if path == 'conversations':
        key = 'data/conversations.json'
    elif path.startswith('conversations/'):
        id = path[len('conversations/'):]
        key = f'data/conversations/{id}.json'
    else:
        return done('No cases hit')

    try:
        # Retrieve the object from S3
        response = s3_client.get_object(Bucket=bucket, Key=key)
        body = response['Body'].read().decode('utf-8')
        return done(None, json.loads(body))
    except Exception as e:
        return done(str(e))

def done(err, res=None):
    if err:
        print(err)

    status_code = '400' if err else '200'
    body = json.dumps(err) if err else json.dumps(res)

    return {
        'statusCode': status_code,
        'body': body,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://ken-serverless-chat-application.s3-website.us-east-2.amazonaws.com'
        }
    }
