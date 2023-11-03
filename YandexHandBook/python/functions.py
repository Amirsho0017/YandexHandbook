def final_price(price, discount=1):
    return price - price * discount / 100


print(final_price(1000, 5))
# Значение скидки не задано, используется значение по умолчанию
print(final_price(1000))


def f(count):
    count += 1
    print(f'Количество вызовов функции равно {count}.')
    return count


count_f = 0
count_f = f(count_f)
count_f = f(count_f)
count_f = f(count_f)


def inc():
    global x
    x += 1
    print(f"Количество вызовов функции равно {x}.")


x = 0
inc()
inc()
inc()
inc()
inc()
print('x = ' + str(x))


def list_modify_1(list_arg):
    # создаём новый локальный список, не имеющий связи с внешним
    list_arg = [1, 2, 3, 4]


def list_modify_2(list_arg):
    # меняем исходный внешний список, переданный как аргумент
    list_arg += [4]


sample_1 = [1, 2, 3]
sample_2 = [1, 2, 3]
list_modify_1(sample_1)
list_modify_2(sample_2)
print(sample_1)
print(sample_2)


def list_modify():
    del sample[-1]


sample = [1, 2, 3]
list_modify()
print(sample)


def only_even(numbers):
    for i, x in enumerate(numbers):
        if x % 2 != 0:
            return False, i
    return True


print(only_even([2, 4, 6]))
print(only_even([1, 2, 3]))


def only_even(numbers):
    for x in numbers:
        if x % 2 != 0:
            return False
    return True


print(only_even([2, 4, 6]))
print(only_even([1, 2, 3]))


def only_even1(numbers):
    result = True
    for x in numbers:
        if x % 2 != 0:
            result = False
            break
    return result


print(only_even1([2, 4, 6]))
print(only_even1([1, 2, 3]))


def add_value(y, list_arg=[]):
    list_arg += [y]
    return list_arg


print(add_value(5))
print(add_value(5, [1, 2, 3]))
print(add_value(1))


def final_price(price, discount=1):
    return price - price * discount / 100


print(final_price(price=1000, discount=5))
print(final_price(discount=10, price=1000))


def add_value(x, list_arg=None):
    if list_arg is None:
        list_arg = []
    list_arg += [x]
    return list_arg


print(add_value(0))
print(add_value(0, [1, 2, 3]))
print(add_value(1))


def final_price(*prices, discount=1):
    return [price - price * discount / 100 for price in prices]


print(final_price(100, 200, 300, discount=5))


def final_price(*prices, discount=1, **kwargs):
    low = kwargs.get("price_low", min(prices))
    high = kwargs.get("price_high", max(prices))
    return [price - price * discount / 100 for price in prices if low <= price <= high]


print(final_price(100, 200, 300, 400, 500, discount=5))
print(final_price(100, 200, 300, 400, 500, discount=5, price_low=200))
print(final_price(100, 200, 300, 400, 500, discount=5, price_high=200))
print(final_price(100, 200, 300, 400, 500, discount=5, price_low=200, price_high=350))


def only_pos(p):
    return p > 0


result = filter(only_pos, [-1, 5, 6, -10, 0])
print(", ".join(str(x) for x in result))


result = filter(str.isalpha, "123ABcd()")
print("".join(result))


def square(x):
    return x ** 2


result = map(square, range(5))
print(", ".join(str(x) for x in result))


result = map(str.lower, ["abCD", "EFGh", "IJkl"])
print("\n".join(result))


result = filter(lambda x: x > 0, [-1, 5, 6, -10, 0])
print(", ".join(str(x) for x in result))

lines = ["abcd", "ab", "abc", "abcdef"]
print(sorted(lines, key=lambda line: len(line)))

lines = ["abcd", "ab", "ba", "acde"]
print(sorted(lines, key=lambda line: (len(line), line)))

lines = ["abcd", "ab", "ba", "acde"]
print(sorted(lines, key=lambda line: (-len(line), line)))
