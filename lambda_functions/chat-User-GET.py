import boto3

# Initialize a Cognito Identity Provider client
cognito = boto3.client('cognito-idp')

def lambda_handler(event, context):
    # Specify the User Pool ID
    user_pool_id = 'us-east-2_Y8pJbuAZY'

    # Initialize an empty list to store usernames
    logins = []

    # Paginate through the list of users
    paginator = cognito.get_paginator('list_users')
    for page in paginator.paginate(
        UserPoolId=user_pool_id,
        AttributesToGet=[],
        Filter='',
        Limit=60
    ):
        for user in page['Users']:
            logins.append(user['Username'])

    return logins
