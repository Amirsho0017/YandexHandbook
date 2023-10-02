
#H
n = int(input())
k = 0
while k < n:
    k += 1
    text = input()
    if 'зайка' in text:
        print(text.index('зайка') + 1)
    else:
        print('Заек нет =(')

#G
print('end')
numbers = input()
print(sum(map(int, numbers.split(" "))))
#F
q = int(input())
k = 0
le = 0
while le < q:
    le += 1
    k += input().count("зайка")
print(k)

#E
text = input()
if text[::-1] == text:
    print('YES')
else:
    print('NO')

#D
li = []
while (text := input()) != "":
    if text[-3:] != '@@@':
        li.append(text.lstrip('##'))

print('\n'.join(li))

#C
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
#B
text = input()
for i in text:
    print(i)

#A
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
