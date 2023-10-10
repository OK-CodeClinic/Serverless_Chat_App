import uuid
import boto3

dynamodb = boto3.client('dynamodb')
table_name = 'Chat-Conversations'

def lambda_handler(event, context):
    # Generate a random UUID
    id = str(uuid.uuid4())
    
    # Extract the users and cognitoUsername from the event
    users = event['users']
    cognito_username = event['cognitoUsername']
    
    # Add the cognitoUsername to the users list
    users.append(cognito_username)
    
    # Create a list of PutItem requests
    records = []
    for user in users:
        record = {
            'PutRequest': {
                'Item': {
                    'ConversationId': {'S': id},
                    'Username': {'S': user}
                }
            }
        }
        records.append(record)

    dynamodb.batch_write_item(
        RequestItems={
            table_name: records
        }
    )
    
    return {
        'id': id
    }
