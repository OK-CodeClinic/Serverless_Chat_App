#  CHATIFY - Serverless Chat Application
## OVERVIEW: 
This project provides an overview of a serverless chat application i developed using AWS services cloud. It is secure, reliable and scalable. The application allows users to engage in chat conversations in real-time. It was accessible at http://chat.kardozo.site.

## OBJECTIVE:
- Cost-Efficiency
- Scalability
- Flexible System
- Maximum Security
- Reduced Operational Overhead
- API-Reach Approach
- Global Reach
- Elasticity
- Serverless Architecture
- Faster Development

### AWS Services Used;
- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon API Gateway
- Amazon Cognito
- Amazon CloudFront
- AWS WAF




## ARCHITECTURE



#### This is exactly what happen behind the scene
- When a user accesses ```https://chatify.kardozo.site```, the request is initially directed to Amazon CloudFront, which acts as the content delivery network (CDN).
- CloudFront, with its cache at edge locations, retrieves the frontend of the chat application from the S3 bucket, where it's hosted.
- AWS WAF provide extra layer of security by protecting the chat application against web application threats and attacks.

- Amazon Cognito plays a crucial role in user authentication and management. When a user creates an account or logs in, Cognito triggers specific AWS Lambda functions that manage user-related tasks.

- API: When a user interacts with your chat application through the URL, their actions trigger specific API requests (GET/POST).

- Lambda functions execute the code to manage chat conversations, messages, and user interactions. 

- DynamoDB serves as the database for the chat application, storing conversation data, message history, timestamp, user information and other essential information.

- The Lambda functions read and write data to DynamoDB, ensuring real-time chat functionality


### PREREQUISTIES
- AWS Account
-  Chat app files (html ,js and css files)






## STEP BY STEP; How its done



## OUTCOME
Website working and running securely
