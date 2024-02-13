import json

def lambda_handler(event, context):
    step_function_result = str(event['result'])
    
    return {
       'body': step_function_result
    }
