# Define a dictionary with exchange rates
# These rates are just examples, in a real-world application you would retrieve current rates from an API
exchange_rates = {
    'USD': 1.0,        # US Dollar
    'EUR': 0.85,       # Euro
    'GBP': 0.75,       # British Pound
    'INR': 74.0,       # Indian Rupee
    'JPY': 110.0,      # Japanese Yen
    'AUD': 1.4,        # Australian Dollar
    'CAD': 1.25,       # Canadian Dollar
}

def convert_currency(amount, from_currency, to_currency):
    # Convert the amount to USD
    amount_in_usd = amount / exchange_rates[from_currency]
    # Convert the USD amount to the target currency
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    return converted_amount

# Get user input for amount and currencies
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (e.g., USD, EUR): ").upper()
to_currency = input("Enter the currency to convert to (e.g., USD, EUR): ").upper()

# Check if the provided currencies are supported
if from_currency in exchange_rates and to_currency in exchange_rates:
    # Perform the conversion
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
else:
    print("One of the currencies is not supported.")
