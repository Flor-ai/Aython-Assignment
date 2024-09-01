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

def generate_collatz_sequence(num):
    print(f"Collatz sequence starting with {num}:")
    while num != 1:
        print(num, end=" -> ")
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    print(num)  # Print the last number 1 without the arrow.

# Input
starting_number = get_positive_integer("Enter a positive integer to start the Collatz sequence: ")

# Processing & Output
generate_collatz_sequence(starting_number)
