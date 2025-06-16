TTEC DIGITAL ASSIGNMENT

1. Overview:

Given a phone number, this module attempts to transform it into one or more possible vanity number representations using the standard phone keypad. It generates letter combinations that correspond to the numeric input and selects the best ones based on fixed criteria.

Currently, everything works locally and can be tested as a standalone Python script. Future steps include integrating it with AWS Lambda and DynamoDB.

2. How it works

First, I created a phone keypad mapping from each digit to its corresponding letters (e.g., 2 → ABC). The script then generates all possible letter combinations for a given phone number.

Since AWS integration is not yet functional, the script currently returns the first n combinations labeled as the “best.” Once AWS is connected, I plan to use an English dictionary to prioritize combinations that form valid words.

3. File Structure

At the moment, the script is contained in a single file: vanity_numbers.py.

4. How to run the code

Simply run the script using: python vanity_numbers.py

5. Implementation notes

The pick_best() function is currently semi-functional, as it depends on AWS connectivity for full functionality. I use itertools.product to generate the combinations.

6. Challenges so far

The main issue has been connecting to AWS. My bank is blocking payments to AWS, so my account setup hasn’t been completed yet.

7. Next steps

Resolve AWS account/payment issue

Integrate code with an AWS Lambda function

Store results in DynamoDB

Make the Lambda function callable from an Amazon Connect flow

Enhance pick_best() with real-word detection using an English dictionary
