# Get a three-digit number from the user
num = int(input("Enter a three-digit number: "))

# Calculate the sum of its digits
digit_sum = sum(int(digit) for digit in str(num))

# Calculate the remainder
remainder = num % digit_sum

# Print the result
print(remainder)
