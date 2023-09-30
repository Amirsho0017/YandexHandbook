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
