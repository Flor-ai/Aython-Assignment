def get_non_negative_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Please enter a valid numeric value.")

# Input
hours = get_non_negative_input("Enter time duration in hours: ")

# Processing
minutes = hours * 60
seconds = hours * 3600

# Output
print(f"The time duration is {minutes:.2f} minutes or {seconds:.2f} seconds.")
