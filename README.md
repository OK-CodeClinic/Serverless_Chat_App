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
- [Download frontend files](https://github.com/OK-CodeClinic/Serverless_Chat_App/tree/main)






## STEP BY STEP: How its done;
### Step-1:     S3 Bucket
- Set up s3 bucket, and upload the application frontend files.
  ![Screenshot (285)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/7cc080bb-b243-4f04-bf83-785b5ec6a0f4)

- Enable s3 website hosting.
  ![Screenshot (286)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/53c5ab43-6e03-49c2-8d28-b1ea9683de1d)


### Step -2: Dynamo DB
- Table 1: Chat-Conversation: Make ```ConversationId```  as the PArtition key, and ```Username``` as the Sort Key. 
- Table 2: Chat-Messages: Make ```ConversationId```  as the PArtition key, and ```Timestamp``` as the Sort Key

  ![Screenshot (287)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/92194c2f-3102-4985-84ad-191dbbda8d11)

- Create Index for table 1: Username-ConversationId-index
  ![Screenshot (288)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/380338a1-deda-426e-83a3-040ae70e287f)



### Step-2: Lambda functions
- Create IAM Roles and Policies that will let Lambda Function Communucate with Dyanmo Db, Cognito and API Gateway.
- The Roles should be looking like this;

- To set up Lambda function, - [Lambda Functions Documentation of this project](https://github.com/OK-CodeClinic/Serverless_Chat_App/tree/main/lambda_functions)
- The Functions should be looking like this;
- Always Test your Lambda Functions
  ![Screenshot (289)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/5bae04c7-b1f5-4897-9d73-7c866d15f37f)


#### Step -3: Set Up Cognito for Manage Users
- Create a Cognito User Pool
  ![Screenshot (290)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/7749ae7f-fcc7-4643-b16a-49a2d2d490fa)

- Customize the Hosted UI to best fit for you. Or choose the Cognito Hosted Public UI.
- Configure App Client settings.


### Step-4:    Set Up API Gateway:
- Check the [API Documentation](https://github.com/OK-CodeClinic/Serverless_Chat_App/blob/main/API%20Documentation/Chat-API-prod-swagger.yaml)
- Create  API Resource: Conversations, Id and Users.
- Create APi methods (GET/POST)
- Attach API methods to trigger Lambda_functions.
- Modify with models and Mapping Templates at the approriate Method and request.
   ![Screenshot (293)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/c7874122-4438-4e7a-98d2-7b4ad91b0dff)

- Test the API if its fetching

- All API should be like this;
   ![Screenshot (292)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/e2dbe33f-6479-47c4-beec-03c1899018b6)

- Always enable CORS for all the Resources. Let the APi allow other domain to access the the Reources;
```
{
  "origin": "specify-the-s3-bucket-url-hosting-the-frontend",
  "methods": ["GET", "POST", "OPTION",],
  "allowedHeaders": ["Authorization", "Content-Type"]
}
```
- Deploy API
- Export the API as swagger and test all your API if giving the right response.. Test it
  ![Screenshot (296)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/833838be-2088-427e-87ae-57ab96b22f41)
  

- Generate SDK
  ![Screenshot (295)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/dd891756-dd8b-4e48-8904-6f708a4fec30)

  

- Set Up Authroizer, and make cognito the Authorizer of the API
  ![Screenshot (294)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/2078bf82-027b-41ba-92c7-15049cb053ff)


### Step 5: SDK to S3
- Unzip SDK folder and update APi into the ```/js``` object directory of the s3 bucket
  ![Screenshot (297)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/46154fe1-5dc8-4f53-b8d7-f099651b3d72)


### Step-6: CloudFront Distribution and WAF
- Create an Origin Acccess Control as S3
  ![Screenshot (298)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/250ac305-608f-46a3-b952-3afda721895f)
  

- To create a Distribution: Make s3 the origin of the Distribution
  ![Screenshot (301)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/50b42691-e1ad-422a-b61f-563b27300aaa)

- Route http traffic to https
- Enable custom domain; set your domain url
- Add domain SSL certiicate for Maximum security
- Set Document Root to ```/index.html```
  ![Screenshot (300)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/fd6f992e-3a05-4ca8-9afb-191d6e613fb7)

- Enable WAF to add Extra layer of Security to the app
  ![Screenshot (302)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/9fc3ae1d-28de-41c4-8f1b-800fb619ced5)

- Update s3 Bucket Policy to allow Cloudfront to access web files.

### Step -7: Configure Custom domain
- The domain used in cloudfront; in my case i use Godaddy. Open DNS management console
  ![Screenshot (304)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/b9d8dbc8-d9fa-4698-b836-182973ebe93d)

- Add the cloudfront distribution url as a CNAME target in the DNS record.
  ![Screenshot (303)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/e02c364d-2694-444d-a153-250cf7640fcc)


- Use the CNAME name pointing to your website url to access the cloudfront resource. 
- Then boom!



### OUTCOME
![Screenshot (306)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/cdd0214a-863f-4567-a602-ec39729772ea)


![Screenshot (307)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/6ecb75b8-b348-4dcb-b9e8-4311635550e2)


![Screenshot (308)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/6cf2497c-07c9-4a24-b283-183140104b1a)








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
  ![Screenshot (312)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/2e389575-1067-467e-8f7a-8711b5539d86)
  ![Screenshot (313)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/5744cd64-56e0-44f2-abd3-6c3b949d9c9f)


#### DynamoDB:

- Read and write capacity units consumed
- Throttled requests
- Table and index metrics 
- Conditional check failed requests

#### Amazon S3:

- Bucket requests (GET, POST)
- Bucket size
  ![Screenshot (311)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/dac2c097-61bc-4c6c-904f-0a4df9433a92)


#### Amazon CloudFront:

- Cache hit rate
- Data transfer (data in/out)
- Viewer response time
- HTTP status codes
  ![Screenshot (309)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/401aad97-4400-422e-8aa9-19f405cf19ee)




#### Amazon Cognito:

- Sign-up and sign-in success and failure rates
- User pool metrics
- User authentication history
#### AWS WAF 

- Requests blocked
- WebACL rule violations
- Top rule match count
  ![Screenshot (310)](https://github.com/OK-CodeClinic/Serverless_Chat_App/assets/100064229/727761fc-b44e-442f-9657-d963c32f3e40)


### CONCLUSION
Chatify Serverless Chat App utilizes Amazon S3 for hosting, AWS Lambda functions for application logic, Amazon DynamoDB for data storage, and Amazon Cognito for user management. AWS CloudFront and WAF enhance security, making it a cost-efficient, high-performance chat solution with global reach.


## Author

- [Kehinde Omokungbe](https://www.github.com/OK-CodeClinic)



## Purpose
This is for leaning purpose only.
