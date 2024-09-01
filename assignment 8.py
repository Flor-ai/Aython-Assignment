def get_valid_marks(subject_name):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject_name}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(average_marks):
    if average_marks >= 90:
        return 'A'
    elif 80 <= average_marks < 90:
        return 'B'
    elif 70 <= average_marks < 80:
        return 'C'
    elif 60 <= average_marks < 70:
        return 'D'
    else:
        return 'F'

# Input
subject1 = get_valid_marks("Subject 1")
subject2 = get_valid_marks("Subject 2")
subject3 = get_valid_marks("Subject 3")

# Processing
average_marks = (subject1 + subject2 + subject3) / 3
grade = calculate_grade(average_marks)

# Output
print(f"Your average marks are: {average_marks:.2f}")
print(f"Your grade is: {grade}")
