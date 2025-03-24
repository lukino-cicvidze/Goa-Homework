# Get a three-digit number from the user
num = int(input("Enter a three-digit number: "))

# Calculate the sum of its digits
sum_of_digits = (num // 100) + ((num // 10) % 10) + (num % 10)

# Calculate the remainder
remainder = num % sum_of_digits

# Print the result
print(remainder)
