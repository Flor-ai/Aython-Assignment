def get_positive_integer(prompt):
    while True:
        try:
            age = int(input(prompt))
            if age > 0:
                return age
            else:
                print("Please enter a positive integer for the age.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def classify_age(age):
    if age < 18:
        return "Minor"
    elif age > 65:
        return "Senior citizen"
    else:
        return "Adult"

# Input
age = get_positive_integer("Enter your age: ")

# Processing
category = classify_age(age)

# Output
print(f"Based on your age, you are classified as: {category}")
