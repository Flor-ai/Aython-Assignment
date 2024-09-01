import math

def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid numeric value.")

# Input
x1 = get_numeric_input("Enter x1: ")
y1 = get_numeric_input("Enter y1: ")
x2 = get_numeric_input("Enter x2: ")
y2 = get_numeric_input("Enter y2: ")

# Processing
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Output
print(f"The distance between the two points is: {distance:.2f}")
