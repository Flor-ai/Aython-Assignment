def is_palindrome(s):
    # Base case: if the string is empty or has one character
    if len(s) <= 1:
        return True
    # Compare the first and last characters
    if s[0] != s[-1]:
        return False
    # Recursive case: check the substring excluding the first and last characters
    return is_palindrome(s[1:-1])

# Example usage
user_string = input("Enter a string to check if it is a palindrome: ")

if is_palindrome(user_string):
    print(f'"{user_string}" is a palindrome.')
else:
    print(f'"{user_string}" is not a palindrome.')
