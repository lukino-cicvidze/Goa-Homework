# პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს და შემოწმებს, არის თუ არა ლუწი ან კენტი
number = int(input("3: "))

# შემოწმება, თუ რიცხვი ლუწია
if number % 2 == 0:
    for _ in range(10):  # 10-ჯერ გამოტანა "yes"
        print("Yes")
else:
    print("No")