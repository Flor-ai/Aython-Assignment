# Fixed exchange rates for demonstration purposes
exchange_rates = {
    "USD_EUR": 0.85,
    "EUR_USD": 1.18,
    "USD_GBP": 0.75,
    "GBP_USD": 1.33,
    "EUR_GBP": 0.88,
    "GBP_EUR": 1.14
}

def get_valid_currency_pair():
    while True:
        print("Available currency pairs:")
        print("1. USD to EUR")
        print("2. EUR to USD")
        print("3. USD to GBP")
        print("4. GBP to USD")
        print("5. EUR to GBP")
        print("6. GBP to EUR")
        
        choice = input("Choose a currency pair (e.g., 'USD_EUR'): ").upper()
        
        if choice in exchange_rates:
            return choice
        else:
            print("Invalid currency pair. Please try again.")

def get_non_negative_amount():
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount >= 0:
                return amount
            else:
                print("Please enter a non-negative amount.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Input
currency_pair = get_valid_currency_pair()
amount = get_non_negative_amount()

# Processing
converted_amount = amount * exchange_rates[currency_pair]

# Output
print(f"The converted amount is: {converted_amount:.2f} in the target currency.")
