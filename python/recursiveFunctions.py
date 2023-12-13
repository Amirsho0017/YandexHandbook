from functools import lru_cache
from sys import setrecursionlimit
from timeit import timeit


@lru_cache(maxsize=1000)
def fib(n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)


print(f"Среднее время вычисления: "
      f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 6)} с.")


def fib(n):
    if n not in cash:
        cash[n] = fib(n - 1) + fib(n - 2)
    return cash[n]


setrecursionlimit(2000)
cash = {0: 1, 1: 1}
print(f"Среднее время вычисления: "
      f"{round(timeit('fib(1000)', number=10, globals=globals()) / 10, 6)} с.")


def fib(n):
    if n not in cash:
        cash[n] = fib(n - 1) + fib(n - 2)
    return cash[n]


cash = {0: 1, 1: 1}
print(f"Среднее время вычисления: "
      f"{round(timeit('fib(1000)', number=10, globals=globals()) / 10, 6)} с.")


def fib(n):
    global count
    count += 1
    if n not in cash:
        cash[n] = fib(n - 1) + fib(n - 2)
    return cash[n]


count = 0
cash = {0: 1, 1: 1}
print(f"Среднее время вычисления: "
      f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 6)} с.")


def fib(n):
    global count
    count += 1
    if n not in cash:
        cash[n] = fib(n - 1) + fib(n - 2)
    return cash[n]


count = 0
cash = {0: 1, 1: 1}
print(f"35-е число Фибоначчи равно: {fib(35)}.")
print(f"Количество вызовов рекурсивной функции равно: {count}.")


def fib(n):
    global count
    count += 1
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)


count = 0
print(f"35-е число Фибоначчи равно: {fib(35)}.")
print(f"Количество вызовов рекурсивной функции равно: {count}.")


def fib(n):
    f_1, f = 1, 1
    for i in range(n - 1):
        f_1, f = f, f_1 + f
    return f


print(f"Среднее время вычисления: "
      f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 3)} с.")


def fib(n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)


print(f"Среднее время вычисления: "
      f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 3)} с.")


def fact(n):
    if n == 0:  # 0! = 1
        return 1
    return fact(n - 1) * n  # n! = (n - 1)! * n


print(fact(5))


def fib(n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(3))


def fact(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


print(fact(10))
