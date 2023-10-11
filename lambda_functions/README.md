## What does these functions do?

#### Chat-Conversations-GET.py
This Lambda function is designed to fetch and assemble data related to chat conversations and their participants, and it returns this information as a JSON response.

#### Chat-Conversations-POST.py
This Lambda function is designed to create a new conversation in a DynamoDB table ('Chat-Conversations') by generating a unique ConversationId (UUID) and adding the provided users (including the 'cognitoUsername') to the conversation. It returns the generated UUID as a response.

#### Chat-Messages-GET.py
This Lambda function is designed to retrieve chat messages from a specific conversation and provide additional details about the conversation, including its participants. It performs an authorization check to ensure that the user has access to the conversation and returns the conversation details as a JSON response.

#### Chat-Messages-POST.py
This Lambda function is designed to receive a chat message along with the conversation ID, generate a timestamp, and insert a new message item into a DynamoDB table named 'Chat-Messages'. This allows for the storage of chat messages in the database.

#### Chat-Users-GET.py
This Lambda function fetches a list of usernames from a Cognito User Pool, excluding the provided 'cognitoUsername', and returns this list of usernames. It can be used, for example, to retrieve a list of other users in the same Cognito User Pool. This ensures that a user itself won't be availabale in its friend list.