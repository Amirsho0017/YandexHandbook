#!/usr/bin/env python3
print('Привет, мир!')  # added to PATH, just run sayHello


def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100, b=500)
