
 # პროგრამა, რომელიც სთხოვს მომხმარებელს ტექსტს და რიცხვს
text = input("luka 3: ")
index = int(input("3 (luka): "))

# ამოწმებს რიცხვის სისწორეს
if index > 0 and index <= len(text):
    print(f"ტექსტში პოზიცია {index} შეიცავს ასო: '{text[index - 1]}'")
else:
    print("hello.")


