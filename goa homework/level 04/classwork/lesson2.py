# მომხმარებლისგან რიცხვის მიღება
num = float(input("3: "))  # რიცხვი, როგორც float (თუ დეციმალური რიცხვი)

# შეამოწმეთ რიცხვის პოზიტიურობა, ნეგატიურობა ან 0
if num > 0:
    res = 1  # თუ რიცხვი პოზიტიურია
elif num < 0:
    res = -1  # თუ რიცხვი ნეგატიურია
else:
    res = 0  # თუ რიცხვი 0-ია

# შედეგის გამოჩენა
print(res)