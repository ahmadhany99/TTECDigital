import itertools
import json
import boto3
from datetime import datetime
# Define the mapping of digits to letters on a phone keypad
KEYPAD = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': '0',
    '1': '1'
}

# Function to convert a phone number into possible letter combinations
def phone_to_letters (phone_number, max_combos=100000):
    # Extract digits from the phone number
    digits=[d for d in phone_number if d.isdigit()] #just to know the non-digit char

    # Generate letter options for each digit
    letter_options=[]
    for d in digits:
        if d in KEYPAD:
            letter_options.append(KEYPAD[d])
        else: 
            letter_options.append(d) #just in case if there was an error
    
    # Estimate the total number of combinations
    total_combos=1
    for options in letter_options: # estimating the total number of combos 
        total_combos*=len(options)
    
    # Raise an error if the number of combinations exceeds the maximum allowed
    if total_combos> max_combos:
        raise ValueError(f"Too many combinations ({total_combos}), input number is too long!")
    
    # Generate all possible combinations of letters
    combos= itertools.product(*letter_options) #generate combinations 
    words=[''.join(combo) for combo in combos]

    return words

# Function to load a dictionary of words from a file
def load_dic(word_file_path='20k.txt'):
    # Open the word file and read words into a set
    with open(word_file_path,'r') as f :
        words= set(line.strip().upper() for line in f if line.strip())
    return words

# Function to pick the best word combinations from a list of words
def pick_best(words,dictionary,top_n=5):
    # dummy logic for now until aws is connected 
    scored_words= []

    # Score each word combination based on dictionary matches
    for combo in words:
        score= 0 
        matched_words=[]

        # Iterate through all possible substrings of the word combination
        for i in range(len(combo)):
            for j in range (i+1, len(combo)+1):
                substring= combo[i:j]
                # Check if the substring is in the dictionary and not already matched
                if substring in dictionary and substring not in matched_words:
                    matched_words.append(substring)
                    # Weight the score based on the position of the matched substring
                    if i==0:
                        score+=len(substring)*3 #to weight it higher
                    else:
                        score+=len(substring) # to make it normal weight
                    
        scored_words.append((combo,score,matched_words))

    # Sort the scored words by score and alphabetically
    scored_words.sort(key=lambda x : (-x[1],x[0]))

    top_results=[]
    
    # Extract the top N results
    for word,score,matches in scored_words[:top_n]:
        top_results.append({
            'combo':word,
            'score':score,
            'matched_words': matches
        })
 
    return top_results

if __name__ == "__main__":
    # Define the input phone number
    phone_number = "74663"
    print(f"\nInput phone number: {phone_number}")

    # Load the dictionary
    dictionary=load_dic()
    try:
        # Generate word combinations from the phone number
        words = phone_to_letters(phone_number)
        print(f"\nGenerated {len(words)} combinations")

        # Pick the best word combinations
        best = pick_best(words, dictionary ,top_n=5)
        print("\nTop 5 Vanity Options:\n")
        for idx, result in enumerate(best):
            combo = result['combo'].upper()
            score = result['score']
            matches = ', '.join(result['matched_words']) if result['matched_words'] else 'None'
            print(f"{idx + 1}. {combo:<10} Score: {score}")
            print(f"   Matched words: {matches}\n")
    except ValueError as error:
        # Handle value errors
        print(f"Error: {error}")


def lambda_handler(event, context):
    # Extract the phone number from the event
    phone_number = event['phone_number']
    if not phone_number:
        return {
            'statusCode': 400,
            'body': json.dumps({"error": "Missing Phone number"})
        }
    try:
        # Convert the phone number into possible letter combinations
        words = phone_to_letters(phone_number)

        # Load the dictionary of words
        dictionary = load_dic("20k.txt")

        # Pick the best word combinations from the list of words
        best_words = pick_best(words, dictionary)

        dynamodb = boto3.resource('dynamodb')
        table=dynamodb.Table('VanityCalls')
        table.put_item(
            Item={
                'caller_number': phone_number,
                'timestamp': datetime.now().isoformat(),
                'top_results': best_words
            }
        )
        print("Saved to DynamoDB:", phone_number)
    # Return the best word combinations as a JSON response
        return {
            'statusCode': 200,
            'body': json.dumps({"results":best_words})
    }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }