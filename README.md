#  CHATIFY - Serverless Chat Application
## OVERVIEW: 
This blog provides an overview of a serverless chat application i developed using AWS services cloud. It is secure, reliable and scalable. The application allows users to engage in chat conversations in real-time. It was accessible at http://chatify.kardozo.site.

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




### ARCHITECTURE
  
  ![serverless-chat-architecture](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/7386bfdf-dd01-4293-a285-05e0ae7dc818)





### This is exactly what happen behind the scene;
- When a user accesses ```https://chatify.kardozo.site```, the request is initially directed to Amazon CloudFront, which acts as the content delivery network (CDN).
- CloudFront, with its cache at edge locations, retrieves the frontend of the chat application from the S3 bucket, where it's hosted.
- AWS WAF provide extra layer of security by protecting the chat application against web application threats and attacks.

- Amazon Cognito plays a crucial role in user authentication and management. When a user creates an account or logs in, Cognito triggers specific AWS Lambda functions that manage user-related tasks.

- API: When a user interacts with the chat application through the URL, their actions trigger specific API requests (GET/POST).

- Lambda functions execute the code to manage chat conversations, messages, and user interactions. 

- DynamoDB serves as the database for the chat application, storing conversation data, message history, timestamp, user information and other essential information.

- The Lambda functions read and write data to DynamoDB, ensuring real-time chat functionality


### PREREQUISTIES
- AWS Account
-  Chat app files (html ,js and css files)






## STEP BY STEP: How its done;
### Step-1:     S3 Bucket
- Set up s3 bucket, and upload the application frontend files.
- Make object public for validations.
- Enable s3 website hosting.

### Step -2: Dynamo DB
- Table 1: Chat-Conversation: Make ```ConversationId```  as the PArtition key, and ```Username``` as the Sort Key. 
- Table 2: Chat-Messages: Make ```ConversationId```  as the PArtition key, and ```Timestamp``` as the Sort Key
- Create Index for table 1: Username-ConversationId-index


### Step-2: Lambda functions
- Create IAM Roles and Policies that will let Lambda Function Communucate with Dyanmo Db, Cognito and API Gateway.
- The Roles should be looking like this;

- To set up Lambda function, - [Lambda Functions Documentation of this project](https://github.com/OK-CodeClinic/Serverless_Chat_App/tree/main/lambda_functions)
- The Functions should be looking like this;
- Always Test your Lambda Functions

#### Step -3: Set Up Cognito for Manage Users
- Create a Cognito User Pool
- Customize the Hosted UI to best fit for you. Or choose the Cognito Hosted Public UI.


### Step-4:    Set Up API Gateway:
- Check the [API Documentation](https://github.com/OK-CodeClinic/Serverless_Chat_App/blob/main/API%20Documentation/Chat-API-prod-swagger.yaml)
- Create  API Resource: Conversations, Id and Users.
- Create APi methods (GET/POST)
- Attach API methods to trigger Lambda_functions.
- Modify with models and Mapping Templates at the approriate Method and request. 
- Test the API if its fetching
- All API should be like this;

- Akways enable CORS for all the Resources. Let the APi allow other domain to access the the Reources;
```
{
  "origin": "specify-the-s3-bucket-url-hosting-the-frontend",
  "methods": ["GET", "POST", "OPTION",],
  "allowedHeaders": ["Authorization", "Content-Type"]
}
```
- Deploy API
- Export the API as swagger

### Step 5: Swagger File
- Add exported APi into the ```/js``` of the s3 object

### Step-6: CloudFront Distribution and WAF
- Create an Origin Acccess Control as S3
- To create a Distribution: Make s3 the origin of the Distribution
- Route http traffic to https
- Enable custom domain; set your domain url
- Add domain SSL certiicate for Maximum security
- Set Document Root to ```/index.html```
- Enable WAF to add Extra layer of Security to the app

### Step -7: Configure Custom domain
- The domain used in cloudfront; in my case i use Godaddy. Open DNS management console
- Add the cloudfront distribution url as a CNAME target in the DNS record.
- Use the CNAME name pointing to your website url to access the cloudfront resource. 
- Then boom!



### OUTCOME







### MONITORING
With the AWS Services used in Chatify, monitoring is an essential aspect of maintaining the health and performance ofthis serverless chat application. 
Proper monitoring can help  detect issues early, optimize performance, and ensure a seamless user experience.

The following resources are monitored:

#### Lambda Functions:

- Invocation count
- Execution duration
- Error rate
- Concurrent executions
- Throttles

#### API Gateway:

- Requests per method
- Error rates
- Latency
- Integration response times
- Integration error rates

#### DynamoDB:

- Read and write capacity units consumed
- Throttled requests
- Table and index metrics 
- Conditional check failed requests

#### Amazon S3:

- Bucket requests (GET, POST)
- Bucket size

#### Amazon CloudFront:

- Cache hit rate
- Data transfer (data in/out)
- Viewer response time
- HTTP status codes

#### Amazon Cognito:

- Sign-up and sign-in success and failure rates
- User pool metrics
- User authentication history
#### AWS WAF 

- Requests blocked

### CONCLUSION
Chatify Serverless Chat App utilizes Amazon S3 for hosting, AWS Lambda functions for application logic, Amazon DynamoDB for data storage, and Amazon Cognito for user management. AWS CloudFront and WAF enhance security, making it a cost-efficient, high-performance chat solution with global reach.


## Author

- [Kehinde Omokungbe](https://www.github.com/OK-CodeClinic)



## Purpose
This is for leaning purpose only.
