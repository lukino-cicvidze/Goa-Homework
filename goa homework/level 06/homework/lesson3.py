# სწორი პაროლი
correct_password = "password123"

# მაქსიმალური ცდა
max_attempts = 3

# ციკლი, რომელიც საშუალებას გვაძლევს შევიყვანოთ პაროლი მხოლოდ სამი მცდელობით
attempts = 0
while attempts < max_attempts:
    # მომხმარებლისგან პაროლის მიღება
    entered_password = input("შეიყვანეთ პაროლი: ")

    # პაროლის შემოწმება
    if entered_password == correct_password:
        print("პაროლი სწორი!")
        break  # პაროლის სწორი შეყვანის შემთხვევაში ციკლი შეწყდება
    else:
        attempts += 1  # მცდელობების ზრდა
        print(f"პაროლი არასწორია. გადმოყვანილი მცდელობები: {attempts}")

    if attempts == max_attempts:
        print("გაყენებული მაქსიმალური მცდელობები. პროგრამა დაიხურება.")
        break  # 3 მცდელობის შემდეგ პროგრამა შეჩერდება
