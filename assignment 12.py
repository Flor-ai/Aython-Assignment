def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_character(prompt):
    while True:
        char = input(prompt)
        if len(char) == 1:
            return char
        else:
            print("Please enter exactly one character.")

def print_triangle(rows, char):
    for i in range(1, rows + 1):
        for j in range(i):
            print(char, end="")
        print()  # Move to the next line after each row

# Input
rows = get_positive_integer("Enter the number of rows for the pattern: ")
pattern_char = get_character("Enter the character to use for the pattern: ")

# Output
print("Pattern:")
print_triangle(rows, pattern_char)
