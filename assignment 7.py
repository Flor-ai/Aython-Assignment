def get_valid_year():
    while True:
        try:
            year = int(input("Enter a year: "))
            if year >= 0:
                return year
            else:
                print("Please enter a valid non-negative year.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def is_leap_year(year):
    # Leap year logic
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input
year = get_valid_year()

# Processing
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
