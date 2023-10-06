import boto3
import time

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Extract values from the event object
    conversation_id = event['id']
    message = event['message']

    # Create a timestamp in milliseconds
    timestamp = str(int(time.time() * 1000))

    # Define the item to be inserted into the DynamoDB table
    item = {
        'ConversationId': {'S': conversation_id},
        'Timestamp': {'N': timestamp},
        'Message': {'S': message},
        'Sender': {'S': event.cognitoUsername}
    }

    # Insert the item into the DynamoDB table
    dynamodb.put_item(
        TableName='Chat-Messages',
        Item=item
    )