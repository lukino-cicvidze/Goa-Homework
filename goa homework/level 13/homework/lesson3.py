# Get an integer from the user
num = int(input("Enter an integer: "))

# Increase the number based on its parity
if num % 2 == 0:
    num += 5  # Increase by 5 if even
else:
    num *= 3  # Multiply by 3 if odd

# Calculate the remainder when divided by 5
remainder = num % 5

# Print the result
print(remainder)
