import json
import boto3
from botocore.exceptions import ClientError

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    path = event['pathParameters']['proxy']

    try:
        if path == 'conversations':
            conversation_data = fetch_conversations()
            return done(None, conversation_data)
        elif path.startswith('conversations/'):
            id = path[len('conversations/'):]
            conversation_data = fetch_conversation_data(id)
            return done(None, conversation_data)
        else:
            return done('No cases hit')
    except ClientError as e:
        return done(str(e))

def fetch_conversations():
    try:
        response = dynamodb.query(
            TableName='Chat-Conversations',
            IndexName='Username-ConversationId-index',
            Select='ALL_PROJECTED_ATTRIBUTES',
            KeyConditionExpression='Username = :username',
            ExpressionAttributeValues={':username': {'S': 'Student'}}
        )
        conversation_ids = [item['ConversationId']['S'] for item in response.get('Items', [])]

        # Fetch last messages and participants for each conversation
        last_messages = fetch_last_messages(conversation_ids)
        participants = fetch_participants(conversation_ids)

        # Prepare the result objects
        result_objs = []
        for id in conversation_ids:
            result_objs.append({
                'id': id,
                'last': last_messages.get(id),
                'participants': participants.get(id, [])
            })

        return result_objs
    except ClientError as e:
        return done(str(e))

def fetch_last_messages(conversation_ids):
    last_messages = {}
    for id in conversation_ids:
        response = dynamodb.query(
            TableName='Chat-Messages',
            ProjectionExpression='ConversationId, #T',
            Limit=1,
            ScanIndexForward=False,
            KeyConditionExpression='ConversationId = :id',
            ExpressionAttributeNames={'#T': 'Timestamp'},
            ExpressionAttributeValues={':id': {'S': id}}
        )
        if response.get('Items'):
            last_messages[id] = int(response['Items'][0]['Timestamp']['N'])
    return last_messages

def fetch_participants(conversation_ids):
    participants = {}
    for id in conversation_ids:
        response = dynamodb.query(
            TableName='Chat-Conversations',
            Select='ALL_ATTRIBUTES',
            KeyConditionExpression='ConversationId = :id',
            ExpressionAttributeValues={':id': {'S': id}}
        )
        participants[id] = [item['Username']['S'] for item in response.get('Items', [])]
    return participants

def fetch_conversation_data(id):
    messages = fetch_messages(id)
    conversation_detail = fetch_conversation_detail(id, messages)
    return {
        'id': id,
        'participants': conversation_detail['participants'],
        'last': messages[-1]['time'] if messages else None,
        'messages': messages
    }

def fetch_messages(id):
    messages = []
    response = dynamodb.query(
        TableName='Chat-Messages',
        ProjectionExpression='#T, Sender, Message',
        ExpressionAttributeNames={'#T': 'Timestamp'},
        KeyConditionExpression='ConversationId = :id',
        ExpressionAttributeValues={':id': {'S': id}}
    )
    for item in response.get('Items', []):
        messages.append({
            'sender': item['Sender']['S'],
            'time': int(item['Timestamp']['N']),
            'message': item['Message']['S']
        })
    return messages

def fetch_conversation_detail(id, messages):
    participants = []
    response = dynamodb.query(
        TableName='Chat-Conversations',
        Select='ALL_ATTRIBUTES',
        KeyConditionExpression='ConversationId = :id',
        ExpressionAttributeValues={':id': {'S': id}}
    )
    for item in response.get('Items', []):
        participants.append(item['Username']['S'])
    return {
        'id': id,
        'participants': participants,
        'last': messages[-1]['time'] if messages else None,
        'messages': messages
    }

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
            'Access-Control-Allow-Origin': '*'
        }
    }
