# N
numbers = input()
deg = int(input())
li = numbers.split(' ')
res = []
for i in li:
    res.append(str(int(i) ** deg))
print(' '.join(res))

# M
q = int(input())
k = 0
li = []
res = []
while k < q:
    k += 1
    li.append(int(input()))
deg = int(input())
for i in li:
    res.append(str(i ** deg))
print('\n'.join(res))

# L
num = int(input())

li = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

while num > len(li):
    li += li
print("\n".join(li[:num]))

# K
pages = int(input())
k = 0
li = []
to_print = []
while k < pages:
    k += 1
    li.append(input())

search_text = input()

for i in li:
    if search_text.lower() in i.lower():
        to_print.append(i)

print('\n'.join(to_print))

# J
maximum = 0
letter = ''
li = ''
while (text := input()) != 'ФИНИШ':
    li += text.replace(' ', '')
li = li.lower()
for i in li:
    if li.count(i) > maximum:
        maximum = li.count(i)
        letter = i
print(letter)

# H
n = int(input())
k = 0
while k < n:
    k += 1
    text = input()
    if 'зайка' in text:
        print(text.index('зайка') + 1)
    else:
        print('Заек нет =(')

# G
print('end')
numbers = input()
print(sum(map(int, numbers.split(" "))))
# F
q = int(input())
k = 0
le = 0
while le < q:
    le += 1
    k += input().count("зайка")
print(k)

# E
text = input()
if text[::-1] == text:
    print('YES')
else:
    print('NO')

# D
li = []
while (text := input()) != "":
    if text[-3:] != '@@@':
        li.append(text.lstrip('##'))

print('\n'.join(li))

# C
length = int(input())
q = int(input())
q1 = 0
li = []
while q1 < q:
    q1 += 1
    li.append(input())
for i in li:
    if len(i) > length:
        print(i[:length - 3] + "...")
    else:
        print(i)
# B
text = input()
for i in text:
    print(i)

# A
count = int(input())
k = 0
li = []

while k < count:
    k += 1
    li.append(input())

for i in li:
    if i[0] not in ["а", "б", "в"]:
        print('NO')
        break
else:
    if li[-1][0] in ["а", "б", "в"]:
        print("YES")
    else:
        print("NO")
