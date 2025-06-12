TTEC DIGITAL ASSIGNMENT

1. Overview:

Given a phone number, this module attempts to transform it into one or more possible vanity number representations with respect to the standard phone keypad: it generates letter combinations that fit the given numeric input and then chooses the best ones according to some fixed criteria.

As for now, it all works locally and could be tested as a standalone Python script. Future steps are definitely a Lambda-DynamoDB integration.

2. How it works

First, I did a phone keypad mapping for each digit to a set of possible letters. For example, 2 -> ABC. Second, this script is based on generating all possible letter combinations for a given phone number. Lastly, for now without a connection of aws I had to do the first n combinations labeled as the “best”. Upon connecting aws, i will use the english dictionary to prioritize valid words.

3. File Structure

For now, I just have my script in vanity_numbers.py.

4. How to run the code

For now, just “python vanity_numbers.py”

5. Implementation notes

Pick_best is just a placeholder but in the future it should match words in an English dictionary . I use "itertools".product to generate combinations.

6. Challenges so far

Aws connection is hard due to my bank blocking aws payment so i cant connect to aws yet.

7. Next steps

Connect Aws.
Integrate my code with aws lambda function
Store results in dynamoDB
Make the lambda callable from amazon connect flow
Improve pick_best() with real word detection
