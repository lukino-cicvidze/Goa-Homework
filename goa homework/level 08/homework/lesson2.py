import random

# ვქმნით ოთხნიშნა საიდუმლო რიცხვს
secret_number = random.randint(1000, 9999)

print("გამოიცანით ოთხნიშნა რიცხვი!")

while True:
    guess = int(input("შეიყვანეთ თქვენი ვარიანტი: "))
    
    if guess == secret_number:
        print("გილოცავთ! სწორად გამოიცანით! 🎉")
        break
    elif guess < secret_number:
        print("უფრო დიდი რიცხვი სცადეთ!")
    else:
        print("უფრო პატარა რიცხვი სცადეთ!")
