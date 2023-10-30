from sys import stdin

# D
lines = []
for line in stdin:
    lines.append(line.rstrip('\n'))
request = lines.pop().lower()
for line in lines:
    if request in line.lower():
        print(line)


# C
for i in stdin.readlines():
    if '#' in i.strip('\n'):
        if '#' == i[0]:
            continue
        else:
            print(i.strip('\n').split('#')[0])
    else:
        print(i.strip('\n'))

# B
avg = 0
q = 0
for i in stdin.readlines():
    q += 1
    k = i.split()
    avg += int(k[-1]) - int(k[1])
print(round(avg / q))


# A
s = stdin.readlines()
summ = 0
lines = [line.rstrip() for line in s]
for i in lines:
    if i is int:
        summ += i
    else:
        for j in i.split(' '):
            summ += int(j)
print(summ)
