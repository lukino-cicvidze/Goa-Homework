# მომხმარებლისგან სიტყვა მიღება
word = input("შეიყვანეთ ნებისმიერი სიტყვა: ")

# 'A' ასოების ფილტრაცია
result = ''.join([char for char in word if char == 'A' or char == 'a'])

# შედეგის გამოყვანა
print(result)