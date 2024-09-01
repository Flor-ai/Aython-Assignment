def get_valid_character():
    while True:
        user_input = input("Enter a single character: ").lower()
        
        if len(user_input) != 1:
            print("Please enter exactly one character.")
        elif not user_input.isalpha():
            print("Please enter a valid letter (a-z).")
        else:
            return user_input

def is_vowel(character):
    return character in 'aeiou'

# Input
character = get_valid_character()

# Processing
if is_vowel(character):
    print(f"{character} is a vowel.")
else:
    print(f"{character} is a consonant.")
