while (text := input("Введите строку (СТОП для остановки): ")) != "СТОП":
    if text == "1":
        break
else:
    print("Цикл завершён")

while input("Введите строку (СТОП для остановки): ") != "СТОП":
    pass
else:
    print("Цикл завершён")

#exclude aa, bb, cc, .....
for i in range(26):
    for j in range(26):
        if i != j:
            print(f"{chr(ord('a') + i)}{chr(ord('a') + j)}")
#exclude aa, bb, cc, .....
for i in range(26):
    for j in range(26):
        if i == j:
            continue
        print(f"{chr(ord('a') + i)}{chr(ord('a') + j)}")

# break in nested loops
flag = False
for i in range(26):
    for j in range(26):
        text = f"{chr(ord('a') + i)}{chr(ord('a') + j)}"
        if text == "ya":
            print(text)
            flag = True
            break
        print(text)
    if flag:
        break

# usage of break
password = "right_password"
while True:
    if input("Введите пароль: ") == password:
        print("Пароль принимается")
        break


# prints letters, ex: aa \n, ab \n .....
for i in range(26):
    for j in range(26):
        print(f"{chr(ord('a') + i)}{chr(ord('a') + j)}")



