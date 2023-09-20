import math
# R
a = int(input())
b = int(input())
c = int(input())

sor = sorted([a, b, c])

print(sor)
a = sor[0]
b = sor[1]
c = sor[2]

# print(val)
if a**2 + b**2 == c**2:
    print('100%')
elif b**2 + a**2 > c**2:
    print('крайне мала')
else:
    print('велика')


# Q
a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c

if a == 0:
    if b == 0:
        print("Infinite solutions" if c == 0 else "No solution")
    else:
        print(f"{-c/b:.2f}" if c != 0 else "0.00")
else:
    if d > 0:
        x1, x2 = sorted([(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)])
        print(f"{x1:.2f} {x2:.2f}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"{x:.2f}")
    else:
        print("No solution")




# P TODO

# O
f_num = input()
s_num = input()

sor = sorted(f_num + s_num)

print(sor[3] + str(int(sor[1]) + int(sor[2]))[-1] + sor[0])

# N
number = input()
sor_num = sorted(number)
maxi = sor_num[2]
avgi = sor_num[1]
mini = sor_num[0]
res = mini + avgi if mini != '0' else avgi + mini

print(res, maxi + avgi)

# M
elfs = input()
gnomes = input()
people = input()

result = int(elfs[0]) if elfs[0] == gnomes[0] == people[0] else int(elfs[1])
print(result)

# L
a = int(input())
b = int(input())
c = int(input())

if a < (b + c) and b < (a + c) and c < (a + b):
    print("YES")
else:
    print("NO")

# K
number = input()
sorted_num = sorted(number)

if int(sorted_num[0]) + int(sorted_num[2]) == int(2 * int(sorted_num[1])):
    print("YES")
else:
    print("NO")

# J
password = int(input())

hundreds = password // 100
tens = (password % 100) // 10
ones = password % 10

sum1 = hundreds + tens
sum2 = tens + ones

print(str(max(sum1, sum2)) + str(min(sum1, sum2)))

# I
name_1 = input()
name_2 = input()
name_3 = input()

print(min(name_1, name_2, name_3))

# H
text = input()

if 'зайка' in text:
    print("YES")
else:
    print("NO")

# G
number = input()
if number[::-1] == number:
    print("YES")
else:
    print("NO")

# F
year = int(input())

if year < 0:
    print('NO')

if abs(year - 2020) % 4 == 0:
    print('YES')
else:
    print('NO')

# E
petya = 7
vasya = 6
petya = petya - 3
vasya = vasya + 3
petya = petya + 2

n = int(input())
m = int(input())

petya += n
vasya += m
if petya > vasya:
    print('Петя')
else:
    print('Вася')

# D
petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya > tolya:
    print("1. Петя", "2. Вася", "3. Толя", sep='\n')
elif vasya > petya > tolya:
    print("1. Вася", "2. Петя", "3. Толя", sep='\n')
elif tolya > vasya > petya:
    print("1. Толя", "2. Вася", "3. Петя", sep='\n')
elif tolya > petya > vasya:
    print("1. Толя", "2. Петя", "3. Вася", sep='\n')
elif petya > tolya > vasya:
    print("1. Петя", "2. Толя", "3. Вася", sep='\n')
else:
    print("1. Вася", "2. Толя", "3. Петя", sep='\n')

# C
petya = int(input())
vasya = int(input())
tolya = int(input())

if max(petya, vasya, tolya) == petya:
    print('Петя')
elif max(petya, vasya, tolya) == vasya:
    print('Вася')
else:
    print('Толя')

# B
petya = int(input())
vasya = int(input())

if petya > vasya:
    print('Петя')
else:
    print('Вася')

# A
print('Как Вас зовут?')
name = input()
print('Здравствуйте, ' + name + '!')
print('Как дела?')
mood = input()
if mood == 'хорошо':
    print('Я за вас рада!')
elif mood == 'плохо':
    print('Всё наладится!')
