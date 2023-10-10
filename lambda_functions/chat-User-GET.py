import boto3

def lambda_handler(event, context):
    # Initialize the Cognito Identity Provider client
    cognito = boto3.client('cognito-idp', region_name='us-east-2')
    
    # Parameters for list_users
    user_pool_id = 'us-east-2_Y8pJbuAZY'
    attributes_to_get = []
    filter_expression = ''
    limit = 60
    
    # Call list_users using the paginator
    logins = []
    paginator = cognito.get_paginator('list_users')
    for page in paginator.paginate(UserPoolId=user_pool_id, AttributesToGet=attributes_to_get, Filter=filter_expression, Limit=limit):
        for user in page['Users']:
            if event['cognitoUsername'] != user['Username']:
                logins.append(user['Username'])
    
    return logins
