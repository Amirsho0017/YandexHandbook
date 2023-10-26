from itertools import chain
from itertools import combinations
from itertools import count
from itertools import cycle
from itertools import islice
from itertools import product

# J


# I
num = int(input())
print(list(product(range(1, num + 1), range(1, num + 1))))

# H
quan = int(input())
li = []
for _ in range(quan):
    li.append(input())
days = int(input())
print('\n'.join(list(islice(cycle(li), days))))

# G
quan = int(input())
li = []
for _ in range(quan):
    li.append(input())
res = list(combinations(li, r=2))
for key, val in res:
    print(f"{key} - {val}")

# F
nominal = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
mast = ['пик', 'треф', 'бубен', 'червей']
mast.remove(input())

res = list(product(nominal, mast))
for key, val in res:
    print(key, val, sep=' ')

# E
f, m, s = input().split(', '), input().split(', '), input().split(', ')
for key, val in enumerate(sorted(list(chain(f, m, s))), 1):
    print(str(key) + '. ' + val)

# D
li = input().split()
print(li)
print(list())

# C
parameters = input().split()
for i in count(float(parameters[0]), float(parameters[2])):
    if i <= float(parameters[1]):
        print(i)
    else:
        break

# B
first_row = input().split(', ')
second_row = input().split(', ')
li = list(zip(first_row, second_row))
for i in li:
    print(' - '.join(i))

# A
text = input().split()
for key, val in enumerate(text, 1):
    print(f"{key}. {val}")
