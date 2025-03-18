import re

def string_clean(text):
    """Removes all numeric characters from the input text while keeping spacing and special characters intact."""
    return re.sub(r'\d', '', text)

# Example usage
print(string_clean('! !'))  # Output: '! !'
print(string_clean('123456789'))  # Output: ''
print(string_clean('This looks5 grea8t!'))  # Output: 'This looks great!'
