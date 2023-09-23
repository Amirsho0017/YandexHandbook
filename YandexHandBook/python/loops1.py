#N


#M
n = int(input())
players = []
k = 0
while k < n:
    players.append(input())
    k += 1

print(min(players))

#L
n = input()

max1 = n[0]
for i in n:
    if max1 < i:
        max1 = i

print(max1)

#K
n = input()
s = 0
for i in n:
    s += int(i)

print(s)


#J
x = 0
y = 0
while (direction := input()) != "СТОП":
    step = int(input())
    if direction == "СЕВЕР":
        y += step
    elif direction == "ЗАПАД":
        x -= step
    elif direction == "ВОСТОК":
        x += step
    elif direction == "ЮГ":
        y -= step

print(x, y, sep='\n')

#I
n = int(input())

f = 1
for i in range(1, n + 1):
    f *= i

print(f)

#H
text = input()
n = int(input())

for i in range(0, n):
    print(text)

#G
a = int(input())
b = int(input())
n1 = a
n2 = b

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(int((n1 * n2) / (a + b)))

#F
a = int(input())
b = int(input())

n = a % b
while a % b != 0:

    if a > b:
        a = a % b
    else:
        b = b % a

print(n)
#E
sum = 0
while (price := float(input())) != 0:
    if price >= 500:
        price = price - price / 10
    sum += price
print(sum)

#D
a, b = int(input()), int(input())
k = ''
step = 1 if a < b else -1
b += step

for i in range(a, b, step):
    k += str(i) + ' '
print(k.lstrip())


#C
a = int(input())
b = int(input())
k = ''

for i in range(a, b + 1):
    k += str(i) + ' '
print(k)

# B
k = 0
while (text := str(input())) != 'Приехали!':
    if "зайка" in text:
        k += 1
print(k)

# A
while (text := input()) != 'Три!':
    print('Режим ожидания...')
print('Ёлочка, гори!')
