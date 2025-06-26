TTEC DIGITAL ASSIGNMENT

1. Overview:

This project takes a phone number and turns it into potential vanity words using a standard phone keypad layout (like 74663 → PHONE). The script generates all valid letter combinations for the digits, scores them based on real dictionary matches, and shows the top results.

Everything runs locally for now and works as a standalone Python script. I’ve also integrated it with AWS Lambda and DynamoDB, and everything is now running smoothly on the cloud.

2. How it works

I built a keypad dictionary mapping digits to letters (2 → ABC, etc.).

The script takes the input number, finds all possible letter combos, and filters out the top-scoring ones based on matches with real English words.

AWS Lambda now handles the backend logic, and the best results are automatically logged in a DynamoDB table called VanityCalls.

3. File Structure

vanity_numbers.py: Main script (used both locally and deployed to Lambda)

20k.txt: Word list (used for matching and scoring)

README.md and vanity_converter.md: Docs like this one

4. How to run the code

Simply run the script using: python vanity_numbers.py

5. AWS Deployment

The same script is deployed as a Lambda function using Python 3.12

The function is tested using manual event input ({"phone_number": "74663"}) through the Lambda console

Results are stored in DynamoDB (VanityCalls table) with timestamp and full result object

6. Challenges faced

Initially had issues creating my AWS account (bank blocks AWS charges)

Also ran into a few formatting problems while cleaning up the Lambda output and DynamoDB record insertion

Debugging Lambda’s output formatting and boto3 JSON structure was tricky but fixed 7. Next steps

Hook Lambda into an Amazon Connect flow so users can say a number and hear back the best vanity options

Improve result formatting on the voice side

7. Why I designed it this way

As I mentioned earlier, the first step was to develop a prototype locally; something extremely minimalistic but functional enough for the creator to test the basic conversion logic and scoring mechanisms. The actual function was soon wrapped as a Lambda and integrated with DynamoDb for storage. I had chosen this because of its nature and because this way, I could easily test individual components before stacking all the AWS integrations.

8. What I did as shortcuts (and wouldn't do in production)

In the script, I used a dictionary file imported it from github and the phone number input.

There is no retry or failure handling implemented in the Lambda function.

There's no integration of API Gateway; currently, the Lambda function gets invoked manually.

IAM roles are a bit too permissive for easy development.

9. If only I had more time...

Link the Lambda function up to Amazon Connect with a functioning phone line and contact flow.

More robust error handling and logging.

Further clean up of output formatting.

Maybe a simple front end and/or CLI tool for actually entering numbers interactively.
