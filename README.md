# State Machine for Calculator

This README provides detailed step-by-step instructions on setting up a state machine for arithmetic operations using AWS Step Functions and AWS Lambda. The state machine will handle four arithmetic operations: addition, subtraction, multiplication, and division.

## Step 1: Create Lambda Functions 

1. Navigate to the AWS Lambda console.
2. Click on "Create function" and choose "Author from scratch".
3. For each arithmetic operation (addition, subtraction, multiplication, division):
   - Enter a function name (e.g., AdditionHandler).
   - Choose a runtime (e.g., Python 3.8).
   - Copy and paste the provided lambda handler code into the function code editor.
   - Click on "Create function".
4. Note down the ARN (Amazon Resource Name) of each Lambda function for later use.

## Step 2: Define State Machine 

1. Open AWS Step Functions in the AWS Management Console.
2. Click on "Create state machine".
3. Enter a name for the state machine.
4. Copy and paste the provided JSON code into the JSON editor.
5. Review the JSON code to ensure:
   - The Lambda function ARNs are correctly referenced in the "FunctionName" field of each task.
   - The input for the state machine includes the operation to be performed (addition, subtraction, multiplication, or division) and the operands (operand1 and operand2).
   - Error handling and retries are configured as per your requirements.

## Step 3: Configure State Machine 

1. Define input for the state machine. The input should contain the following parameters:
   - "operation": The arithmetic operation to be performed (e.g., "addition", "subtraction", "multiplication", "division").
   - "operand1": The first operand for the operation.
   - "operand2": The second operand for the operation.
2. Configure error handling and retries for Lambda function invocations based on your application's requirements. Adjust the "Retry" section in the state machine definition if needed.

## Step 4: Test State Machine 

1. Use the Step Functions console to start an execution of the state machine.
2. Input the required parameters (operation, operand1, operand2) when prompted.
3. Monitor the execution in the Step Functions console to ensure it progresses through the states as expected.
4. Verify the final result returned by the state machine matches the expected result of the arithmetic operation.

## Step 5: Cleanup 

1. Once testing is complete, ensure to delete any resources (state machine, Lambda functions) that are no longer needed to avoid incurring unnecessary costs.

## Additional Considerations: 

- Ensure appropriate IAM permissions are set for the Lambda functions to be invoked by the Step Functions state machine.
- Test thoroughly with various input scenarios to ensure the state machine handles different cases correctly.
- Monitor the execution of the state machine and adjust error handling/retry configurations as necessary based on observed behavior.
- Follow AWS best practices for security, performance, and cost optimization when configuring resources.
