def count_char_occurrences(s: str, char: str) -> int:
    """
    Returns the number of times 'char' appears in 's'.
    """
    return s.count(char)

# Example usage:
print(count_char_occurrences("hello world", "o"))  # Output: 2
print(count_char_occurrences("banana", "a"))      # Output: 3
