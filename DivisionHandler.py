import json

def lambda_handler(event, context):
    # TODO implement
    num1 = event['operand1']
    num2 = event['operand2']
    result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    return { "result": result }
    
