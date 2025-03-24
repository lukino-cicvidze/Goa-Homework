# Get an integer from the user
num = int(input("Enter an integer: "))

# Increase by 1 if the number is odd
if num % 2 != 0:
    num += 1

# Print the final number
print(num)

# Get an integer from the user
num = int(input("Enter an integer: "))

# Use mathematical trick: add 1 if odd, else keep the same
num += num % 2

# Print the final number
print(num)
