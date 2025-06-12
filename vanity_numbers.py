import itertools

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

def phone_to_letters (phone_number):
    digits=[d for d in phone_number if d.isdigit()] #just to know the non-digit char

    letter_options=[]
    for d in digits:
        if d in KEYPAD:
            letter_options.append(KEYPAD[d])
        else: 
            letter_options.append(d) #just in case if there was an error
    
    combos= itertools.product(*letter_options) #generate combinations 
    words=[''.join(combo) for combo in combos]

    return words

def pick_best(words,top_n=5):
    # dummy logic for now until aws is connected 

    return words [:top_n]

if __name__ == "__main__":
    phone_number = "3432141"
    print(f"Input phone number: {phone_number}")

    words = phone_to_letters(phone_number)
    print(f"Generated {len(words)} combinations")

    best = pick_best(words, top_n=5)
    print("Top 5 vanity options:")
    for b in best:
        print(b)

    

