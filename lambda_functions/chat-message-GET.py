import boto3

def lambda_handler(event, context):

    dynamodb = boto3.client('dynamodb', region_name='us-east-2')  
    
    messages = []
    
    paginator = dynamodb.get_paginator('query')
    for page in paginator.paginate(
        TableName='Chat-Messages',
        ProjectionExpression='#T, Sender, Message',
        ExpressionAttributeNames={'#T': 'Timestamp'},
        KeyConditionExpression='ConversationId = :id',
        ExpressionAttributeValues={':id': {'S': event['id']}}
    ):
        for message in page['Items']:
            messages.append({
                'sender': message['Sender']['S'],
                'time': int(message['Timestamp']['N']),
                'message': message['Message']['S']
            })
    
    return load_conversation_detail(event['id'], messages, event.get('cognitoUsername'))

def load_conversation_detail(id, messages, username):
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb', region_name='us-east-2') 
    
    # Initialize participants list
    participants = []
    
    # Query DynamoDB using paginator
    paginator = dynamodb.get_paginator('query')
    for page in paginator.paginate(
        TableName='Chat-Conversations',
        Select='ALL_ATTRIBUTES',
        KeyConditionExpression='ConversationId = :id',
        ExpressionAttributeValues={':id': {'S': id}}
    ):
        for item in page['Items']:
            participants.append(item['Username']['S'])
    
    if username not in participants:
        return "unauthorized"
    
    return {
        'id': id,
        'participants': participants,
        'last': messages[-1]['time'] if messages else None,
        'messages': messages
    }
