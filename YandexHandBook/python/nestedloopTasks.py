
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