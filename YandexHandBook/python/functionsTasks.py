# C
def number_length(number):
    if number < 0:
        return len(str(number)) - 1
    else:
        return len(str(number))


# B
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# A
def print_hello(string):
    print('Hello, ' + string + '!')

