import logging
import sys

#Creating my logger
logger = logging.getLogger(__name__)

#Setting logger lvl to INFO
logger.setLevel(logging.INFO)

#Create a handler 
currency_handler = logging.StreamHandler(sys.stdout)

#Creating a formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

#Assigning the formatter to the currency handler
currency_handler.setFormatter(formatter)

#Assigning the handler to the logger
logger.addHandler(currency_handler)


currencies = {
    "USD": 1.0,       # US Dollar
    "EUR": 0.92,      # Euro
    "GBP": 0.81,      # British Pound
    "JPY": 146.5,     # Japanese Yen
    "AUD": 1.63,      # Australian Dollar
    "CAD": 1.35,      # Canadian Dollar
    "INR": 83.5,      # Indian Rupee
    "CHF": 0.87,      # Swiss Franc
    "CNY": 6.85,      # Chinese Yuan
    "NZD": 1.71       # New Zealand Dollar
}


#Logging the amount
user_input = input("Please enter an amount: ")
try:
    amount = int(user_input)
    logger.info(f"The user has entered {amount}")
except ValueError:
    logger.error(f"Invalid value entered, this program will exit.")
    sys.exit()  

#Displaying avaialble Currencies 
for currency_name,currency_value in currencies.items():
    logger.info(f"{currency_name}, {currency_value}")

#Get the Currency to Convert From:
try:
    currency_to_convert_from = input("Please choose one of the currencies listed above to convert from: ")
    if currency_to_convert_from not in currencies.keys():
        raise ValueError(f"The current currency {currency_to_convert_from} doesnt exist the program will now exit")
    
except ValueError as e:
    logger.error("Invalid Input : {e}")
    sys.exit()

#Get the currency to convert to:
try:
    currency_to_convert_to = input("Please choose a Currency to convert to from above: ")
    if currency_to_convert_to not in currencies.keys():
        raise ValueError(f"The entered {currency_to_convert_to} should be a valid Currency")
    
except ValueError as e:
    logger.error(f"Invalid Input: {e}")
    sys.exit()

#Converting the value to from source currency to destination currency
try:

    amount = int(user_input)
    converting_value = amount * (currencies[currency_to_convert_to] / currencies[currency_to_convert_from])
    logger.info(f"The user entered {amount} {currency_to_convert_from} ")
    logger.info(f"{amount} {currency_to_convert_from} to {currency_to_convert_to} = {converting_value}{currency_to_convert_to}")
except ValueError:
    logger.error("Invalid Input: Please try again")


            


