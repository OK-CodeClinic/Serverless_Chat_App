## Models
These Models are data structure that represents the shape and format of the request and response payloads for your API's methods. Models are essential for defining the structure of data that flows in and out of your API. 
In this project, models in API Gateway play a crucial role in ensuring data consistency, validation, and transformation as data moves between clients, API Gateway, and my backend services.

### What these Models do here?
- Request and Response Validation: They help us define the expected structure of data in the requests that the API receives and the responses that it sends. This enables API Gateway to validate incoming requests to ensure they match the specified model. If a request doesn't conform to the model, API Gateway can reject it before it reaches the backend services, helping to maintain data integrity.

- Transform Data: Here, they also define mapping templates that specify how to transform data between the format expected by your clients and the format expected by your backend services.

- Both Integrations: Models used here are associated with integration configurations. When defining an integration for an API method (GET and POST), I can specify how data should be mapped between the API Gateway model and the backend service's data format. This ensures that the data sent to and received from the backend service is correctly structured.