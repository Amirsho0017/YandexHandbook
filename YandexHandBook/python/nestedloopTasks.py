
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