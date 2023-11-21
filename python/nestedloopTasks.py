# Q palindrome
n = int(input())
k = 0
nums = []
li = 0
while k < n:
    k += 1
    nums.append(str(input()))
for i in nums:
    if i == i[::-1]:
        li += 1
print(li)

# M
n, m = int(input()), int(input())

max_value = n * m

column_width = len(str(max_value))

for i in range(1, n + 1):
    row = []
    for j in range(1, m + 1):
        num = i + (j - 1) * n
        formatted_num = str(num).rjust(column_width)
        row.append(formatted_num)
    print(' '.join(row))


# L
n, m = int(input()), int(input())
max_width = len(str(n * m))

li = []
k = 0

for i in range(1, n * m + 1):
    if k < m:
        li.append(f'{i:>{max_width}}')
        k += 1
    else:
        print(' '.join(li))
        k = 1
        li = [f'{i:>{max_width}}']

print(' '.join(li))

# I
n = int(input())
k = 0
le = []
while k < n:
    k += 1
    num = str(input())
    maxi = num[0]
    for i in num:
        if maxi < i:
            maxi = i
    le.append(maxi)
print(''.join(le))

# H
q = int(input())
k = 0
le = []
maximum = 0
winner = ""
while k < q:
    k += 1
    name = input()
    number = input()
    s = 0
    for i in number:
        s += int(i)
    le.append(s)
    if maximum <= s:
        maximum = s
        winner = name

print(winner)


# G
num = int(input())
start_sec = 3
participant = 1
while participant <= num:
    for i in range(start_sec, 0, -1):
        print(f"До старта {i} секунд(ы)")
    print(f"Старт {participant}!!!")
    participant += 1
    start_sec += 1

# E
quan = int(input())
q = 0
k = 0
while k < quan:
    le = []
    while (st := input()) != "ВСЁ":
        le.append(st)
    k += 1
    if "зайка" in le:
        q += 1
print(q)

# D
quan = int(input())
s = 0
k = 0
while k < quan:
    st = str(input())
    for i in st:
        s += int(i)
    k += 1
print(s)

# B
num = int(input())
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(f"{j} * {i} = {i * j}")

# A
num = int(input())

for i in range(1, num + 1):
    output = []
    for j in range(1, num + 1):
        output.append(str(i * j))
    print(' '.join(output))