from fastapi import FastAPI
import boto3


app = FastAPI()

# Configure AWS credentials
aws_access_key_id = "AKIA56SCV4ZOD2UMAEFT"
aws_secret_access_key = "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"

# Create a boto3 client object with explicit credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

 
# AWS Lambda Configuration
#lambda_client = boto.client('lambda', region_name='us-east-2')
lambda_client = session.client('lambda', region_name='us-east-2')
 
@app.get("/")
def read_root():
    return {"message": "Hello, this is a FastAPI backend!"}
    
@app.get("/process_data")
def process_data():
    # Your logic to process data goes here
    return {"result": "Data processed successfully"}
 
@app.get("/invoke_lambda")
def invoke_lambda():
    try:
        # Replace 'your-lambda-function-name' with the actual name of your Lambda function
        response = lambda_client.invoke(
            FunctionName='cdergpt_turnonEC2',
            InvocationType='RequestResponse'
        )
        # Parse Lambda response
        lambda_response = response['Payload'].read().decode('utf-8')
        return {"lambda_response": lambda_response}
    except Exception as e:
        return {"error": str(e)}

@app.get("/stop_lambda")
def stop_lambda():
    try:
        # Replace 'your-lambda-function-name' with the actual name of your Lambda function
        response = lambda_client.invoke(
            FunctionName='cdergpt_turnoffEC2',
            InvocationType='RequestResponse'
        )
        # Parse Lambda response
        lambda_response = response['Payload'].read().decode('utf-8')
        return {"lambda_response": lambda_response}
    except Exception as e:
        return {"error": str(e)}