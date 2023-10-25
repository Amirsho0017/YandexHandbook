# J
rle = [('a', 2), ('b', 3), ('c', 1)]
print(''.join([i * count for i, count in rle]))

# I
numbers = [1, 1, 3, 1, 10, -2, 4, 6, 7, 1, 2, 7, 0]
print(' - '.join([str(i) for i in sorted(set(numbers))]))

# H
print((''.join([i[0].upper() for i in 'hello world'.capitalize().split()])))

# G
numbers = {}
print({number: [i for i in range(1, number + 1) if number % i == 0] for number in numbers})

# F
text = 'Мама мыла раму!'
print({letter: text.lower().count(letter) for letter in text.lower() if letter.isalpha()})

# E
numbers = [number for number in range(16, 100, 4)]
print({i for i in numbers if i ** 0.5 % 1 == 0})

# D
numbers = [1, 2, 3]
print({i for i in numbers if i % 2 != 0})

# C
sentence = 'Hello world!'
print([len(i) for i in sentence.split()])

# B
n = 4
print([[i * j for j in range(1, n + 1)] for i in range(1, n + 1)])

# A
a = input()
b = input()
numbers = [i**2 for i in range(int(a), int(b) + 1)]
