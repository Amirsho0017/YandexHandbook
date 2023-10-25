from sys import getsizeof
from timeit import timeit
from copy import deepcopy

numbers = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
numbers_copy = deepcopy(numbers)
print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

numbers = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
numbers_copy = [elem[:] for elem in numbers]
print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

numbers = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
numbers_copy = numbers[:]
numbers[0][0] = 10
print(numbers_copy)
print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

x = [1, 2, 3]
y = x[:]
print(x is y)
x[0] = 0
print(x)
print(y)
print(x is y)

x = [1, 2, 3]
y = x
print(x is y)
x[0] = 0
print(x)
print(y)
print(x is y)

x = [1, 2]
y = [1, 2]
print(x == y)
print(x is y)

x = 1
z = x
print(id(x))
print(id(z))
print(x is z)

a = 440
print(id(a))
print(round(timeit("s = '; '.join(str(x) for x in range(10 ** 6))", number=10), 3))
print(round(timeit("s = '; '.join([str(x) for x in list(range(10 ** 6))])", number=10), 3))
# Создаём итератор из одного миллиона целых чисел
numbers_iter = (i for i in range(10 ** 6))
# Выводим количество байт, занятых итератором
print(f"Итератор занимает {getsizeof(numbers_iter)} байт.")
# Создаём список
numbers_list = list(range(10 ** 6))
# Выводим количество байт, занятых списком
print(f"Список занимает {getsizeof(numbers_list)} байт.")


numbers = (int(input()) for i in range(5))
print(numbers)  # <generator object <genexpr> at 0x00000266CEA0CAC0>

countries = {country: capital for country, capital in
             [("Россия", "Москва"),
              ("Беларусь", "Минск"),
              ("Сербия", "Белград")]}
print(countries)

countries = {"Россия": ["русский"],
             "Беларусь": ["белорусский", "русский"],
             "Бельгия": ["немецкий", "французский", "нидерландский"],
             "Вьетнам": ["вьетнамский"]}

mul_lang = [country for country, lang in countries.items() if len(lang) > 1]
print(mul_lang)


text = 'Hello world'
numbers = [ord(i) for i in text]

print(numbers)
matrix = [[int(x) for x in input().split()] for i in range(5)]
print(matrix)

numbers = []
for i in range(5):
    numbers.append(int(input()))
print(numbers)

numbers = [int(input()) for i in range(5)]
print(numbers)

avg = sum(numbers) // len(numbers)
numbers = [el for el in numbers if el > avg]
print(numbers)
