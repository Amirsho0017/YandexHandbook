from sys import stdin

# G
numbers = []
with open(input(), encoding='UTF-8') as input_txt:
    text = input_txt.read().strip('\n')

res = []
for i in text.split('\n'):
    for j in i.split(' '):
        numbers.append(int(j))
res.append(str(len(numbers)))
res.append(str(sum(1 for i in numbers if i > 0)))
res.append(str(min(numbers)))
res.append(str(max(numbers)))
res.append(str(sum(numbers)))
res.append(str(round(sum(numbers) / len(numbers), 2)))
print('\n'.join(res))

# F
lines = []
for line in stdin:
    for word in line.split(' '):
        word = word.strip()
        if word.lower() == word[::-1].lower():
            if word not in lines:
                lines.append(word)
print('\n'.join(sorted(lines)))

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
