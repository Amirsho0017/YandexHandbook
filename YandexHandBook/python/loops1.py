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
