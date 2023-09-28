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