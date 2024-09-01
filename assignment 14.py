def power(base, exponent):
    if exponent == 0:
        return 1  # Any number raised to the power of 0 is 1
    elif exponent > 0:
        result = 1
        for _ in range(exponent):
            result *= base
        return result
    else:  # exponent < 0
        positive_exponent = -exponent
        result = 1
        for _ in range(positive_exponent):
            result *= base
        return 1 / result

# Example usage
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")
