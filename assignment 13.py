def is_palindrome(s):
    s = s.lower()  # Convert to lowercase to ensure case-insensitive comparison
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Input
user_string = input("Enter a string to check if it is a palindrome: ")

# Check and Output
if is_palindrome(user_string):
    print(f'"{user_string}" is a palindrome.')
else:
    print(f'"{user_string}" is not a palindrome.')
