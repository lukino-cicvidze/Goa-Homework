3# მომხმარებლისგან ქულის მიღება
score = int(input("შეიყვანეთ თქვენი პროექტის ქულა: "))

# შეფასების გამოთვლა
if score > 90:
    grade = "A"
elif score > 75:
    grade = "B"
elif score > 60:
    grade = "C"
elif score > 50:
    grade = "D"
elif score > 40:
    grade = "E"
else:
    grade = "F"

# შედეგის გამოყვანა
print(f"თქვენი შეფასება: {grade}")
