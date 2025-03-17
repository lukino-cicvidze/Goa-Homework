# მომხმარებლისგან რიცხვის მიღება
number = int(input("შეიყვანეთ რიცხვი: "))

# დავამოწმოთ არის თუ არა რიცხვი მარტივი
is_prime = True  # საწყისი ნაგულისხმევი მნიშვნელობა არის რომ რიცხვი მარტივია

# თუ რიცხვი 1-ზე ნაკლებია, ის არ შეიძლება იყოს მარტივი
if number < 2:
    is_prime = False
else:
    # დავამოწმოთ რიცხვი 2-დან number-1-მდე
    for i in range(2, number):
        if number % i == 0:  # თუ რიცხვი იყოფა i-ით, ის არ არის მარტივი
            is_prime = False
            break

# შედეგის გამოქვეყნება
if is_prime:
    print("your number is a prime")
else:
    print("your number is not a prime")