# პაროლის ცვლადი
correct_password = "mypassword123"  # შეგიძლიათ შეცვალოთ ნებისმიერი პაროლით

# მომხმარებლის პაროლის მიღება და შემოწმება
while True:
    user_password = input("luka123: ")  # მომხმარებელი აწვდის პაროლს
    if user_password == correct_password:
        print("პაროლი სწორია!")
        break  # სწორ პაროლზე გამოსვლა ციკლიდან
    else:
        print("პაროლი არასწორია, სცადეთ კვლავ.")