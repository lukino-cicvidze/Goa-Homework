def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    
    if 90 <= avg <= 100:
        return 'A'
    elif 80 <= avg < 90:
        return 'B'
    elif 70 <= avg < 80:
        return 'C'
    elif 60 <= avg < 70:
        return 'D'
    else:
        return 'F'

# Example usage
print(get_grade(95, 90, 93))  # Output: 'A'
print(get_grade(70, 75, 79))  # Output: 'C'
print(get_grade(50, 60, 58))  # Output: 'F'