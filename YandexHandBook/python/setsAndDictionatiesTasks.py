# F
# num1 = int(input())
# num2 = int(input())
# set1 = set()
# set2 = set()
#
# k = 0
# while k < num1:
#     k += 1
#     set1.add(input())
#
# k = 0
# while k < num2:
#     k += 1
#     set2.add(input())
#
# if len(set1 ^ set2) == 0:
#     print('Таких нет')
# else:
#     print('\n'.join(sorted(set1 ^ set2)))


# E
num1 = int(input())
num2 = int(input())
set1 = set()
set2 = set()

k = 0
while k < num1 + num2:
    k += 1
    a = input()
    set1.add(a)

    set1.add(input())

k = 0
while k < num2:
    k += 1
    set2.add(input())

print(set1, set2)
if len(set1 ^ set2) == 0:
    print('Таких нет')
else:
    print(len(set1 ^ set2))

# D
num1 = int(input())
num2 = int(input())
set1 = set()
set2 = set()

k = 0
while k < num1:
    k += 1
    set1.add(input())

k = 0
while k < num2:
    k += 1
    set2.add(input())

if len(set1 & set2) == 0:
    print('Таких нет')
else:
    print(len(set1 & set2))


# C
k = 0
num = int(input())
set1 = set()
while k < num:
    k += 1
    for i in input().split(' '):
        set1.add(i)
print('\n'.join(set1))

# B
print(''.join(set(input()) & set(input())))

# A
text = input()
text = set(text)
print(''.join(text))