def count_char_occurrences(s: str, char: str) -> int:
    """Returns the number of times char occurs in the string s."""
    return s.count(char)

# Example usage
print(count_char_occurrences("hello", "l"))  # Output: 2
print(count_char_occurrences("apple", "p"))  # Output: 2
print(count_char_occurrences("banana", "a"))  # Output: 3