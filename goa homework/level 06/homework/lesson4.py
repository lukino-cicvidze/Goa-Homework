# მომხმარებლისგან სტრინგის მიღება
user_string = input("შეიყვანეთ რაიმე სტრინგი: ")

# შემოტრიალებული სტრინგის მისაღებად for ციკლი
reversed_string = ""
for char in user_string:
    reversed_string = char + reversed_string  # თითოეული სიმბოლო თავდაპირველ სტრინგში იდოს წინ

# შედეგის გამოყვანა
print("შემოტრიალებული სტრინგი:", reversed_string)