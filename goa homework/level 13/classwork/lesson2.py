def abbrev_name(name):
    return ".".join([word[0].upper() for word in name.split()])

# Example usage:
print(abbrev_name("Sam Harris"))  # Output: S.H
print(abbrev_name("patrick feeney"))  # Output: P.F
