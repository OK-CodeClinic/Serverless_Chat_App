import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    conversation_ids = []
    paginator = dynamodb.get_paginator('query')
    for page in paginator.paginate(
        TableName='Chat-Conversations',
        IndexName='Username-ConversationId-index',
        Select='ALL_PROJECTED_ATTRIBUTES',
        KeyConditionExpression='Username = :username',
        ExpressionAttributeValues={':username': {'S': 'Student'}}
    ):
        for item in page['Items']:
            conversation_ids.append(item['ConversationId']['S'])

    # Load last messages
    lasts = load_convos_last(conversation_ids)

    # Load conversation participants
    parts = load_convo_participants(conversation_ids)

    # Construct the response
    response = []
    for id in conversation_ids:
        response.append({
            'id': id,
            'last': lasts[id],
            'participants': parts[id]
        })

    return response

def load_convos_last(ids):
    result = {}
    for id in ids:
        response = dynamodb.query(
            TableName='Chat-Messages',
            ProjectionExpression='ConversationId, #T',
            Limit=1,
            ScanIndexForward=False,
            KeyConditionExpression='ConversationId = :id',
            ExpressionAttributeNames={'#T': 'Timestamp'},
            ExpressionAttributeValues={':id': {'S': id}}
        )
        if len(response['Items']) == 1:
            result[id] = int(response['Items'][0]['Timestamp']['N'])
    return result

def load_convo_participants(ids):
    result = {}
    for id in ids:
        participants = []
        paginator = dynamodb.get_paginator('query')
        for page in paginator.paginate(
            TableName='Chat-Conversations',
            Select='ALL_ATTRIBUTES',
            KeyConditionExpression='ConversationId = :id',
            ExpressionAttributeValues={':id': {'S': id}}
        ):
            for item in page['Items']:
                participants.append(item['Username']['S'])
        result[id] = participants
    return result
