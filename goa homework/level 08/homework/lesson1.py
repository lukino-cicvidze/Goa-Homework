
while True:
    num = int(input("შეიყვანეთ რიცხვი (1-50): "))
    if 1 <= num <= 50:
        break
    print("გთხოვთ, შეიყვანოთ რიცხვი 1-დან 50-მდე.")

print(f"{num}-ის ჯერადები 100-ის ჩათვლით:")
for i in range(num, 101, num):
    print(i)

