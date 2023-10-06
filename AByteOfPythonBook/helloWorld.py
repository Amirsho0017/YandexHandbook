#!/usr/bin/env python3
import os
import sys


if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')


print(os.getcwd())

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')
def printMax(x, y):
    """Выводит максимальное из двух чисел. Оба значения должны быть целыми числами."""

    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')


printMax(3, 5)
print(printMax.__doc__)

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y


print(maximum(2, 3))


def total(a=5, *numbers, **phonebook):
    print('a', a)
    for single_item in numbers:
        print('single_item', single_item)
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))

print('Привет, мир!')  # added to PATH, just run sayHello


def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100, b=500)
