#A
print('Привет, Яндекс!')

#B
username = input('Как Вас зовут?')
print('Привет, ' + username)

#C
text = input()
print((text + "\n") * 3)
# print(text)
# print(text)
# print(text)

#D
money = float(input())
print(int(money - 2.5 * 38))

#E
price = int(input())
weight = int(input())
money = int(input())

print(money - price * weight)

#F
name = str(input())
price = int(input())
weight = int(input())
money = int(input())
print('Чек')
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {price * weight}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {money - price * weight}руб")

#G
n = int(input())
phrase = 'Купи слона!'
print((phrase + "\n") * n)

#H
n = int(input())
text = input()
print((f"Я больше никогда не буду писать \"{text}\"!" + '\n') * n)

#I
n = int(input())
m = int(input())
print(int(m / 2 * n))

#J
name = input()
number = input()
print(f"Группа №{number[0]}. \n{number[2]}. {name}. \nШкафчик: {number}. \nКроватка: {number[1]}.")

#K
number = input()
print(number[1] + number[0] + number[3] + number[2])

#L
#TODO


#M
children = int(input())
cake = int(input())
print(cake // children, cake % children, sep="\n")

#N
red = int(input())
green = int(input())
blue = int(input())

print(sum([green, red, blue]) - green + 1)

#O
N = int(input())  # Часы
M = int(input())  # Минуты
T = int(input())  # Время доставки в минутах

current_time_minutes = N * 60 + M

delivery_time_minutes = current_time_minutes + T

hours = delivery_time_minutes // 60
minutes = delivery_time_minutes % 60

if hours >= 24:
    hours %= 24

print(f"{hours:02}:{minutes:02}")

#P
a = int(input())
b = int(input())
c = int(input())

print((b - a) / c)

#Q
summ = int(input())
binary_number = int(input(), 2)
print(summ + binary_number)

#R
binary_number = int(input(), 2)
money = int(input())
print(money - binary_number)

#S
name = input()
price = int(input())
weight = int(input())
money = int(input())

title = "================Чек================"
end = "==================================="
merchantText = f"Товар:{name: >29}"
priceText = "Цена: " + f"{weight}кг * {price}руб/кг".rjust(29, ' ')
totalText = f"Итого:{weight * price: >26}руб"
moneyText = f"Внесено:{money: >24}руб"
changeText = f"Сдача:{money - weight * price: >26}руб"

print(title, merchantText, priceText, totalText, moneyText, changeText, end, sep="\n")

#T
weight = int(input())
price = int(input())
price_1 = int(input())
price_2 = int(input())

k1 = (price_1 * weight - weight * price) // (price_1 - price_2)
print(weight - k1, k1)




