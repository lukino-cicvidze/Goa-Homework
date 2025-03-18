def add_length(s):
    """Takes a string and returns a list where each word is followed by its length."""
    return [f"{word} {len(word)}" for word in s.split()]

# Example usage
print(add_length("apple ban"))  # Output: ["apple 5", "ban 3"]
print(add_length("you will win"))  # Output: ["you 3", "will 4", "win 3"]
