import re

def extract_numerical_value(text):
    # Define regular expression patterns to match the numerical values and symbols
    patterns = [
        r'(\d+(\.\d+)?)\s*GB',  # Match GB values
        r'(\d+(\.\d+)?)\s*MB',  # Match MB values
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = float(match.group(1))  # Extract numerical value
            unit = match.group(0)[-2:].upper()  # Extract unit (GB or MB) and convert to uppercase
            if unit == 'MB':
                value /= 1024  # Convert MB to GB
            return value

    # If no match is found, return None
    return None

def format_price(price_text):
    # Regular expression to find any number with optional decimal points and commas
    price_regex = r'\d+(?:,\d{3})*(?:\.\d+)?'
    
    # Find all numbers in the text
    prices = re.findall(price_regex, price_text)
    
    # If multiple numbers are found, take the first one
    if prices:
        formatted_price = prices[0]
        # If the price contains a comma, remove it
        formatted_price = formatted_price.replace(',', '')
        return formatted_price
    else:
        return None
