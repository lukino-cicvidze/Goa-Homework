def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9

# Example usage
print(simple_multiplication(4))  # Output: 32 (even)
print(simple_multiplication(5))  # Output: 45 (odd)