# B
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# A
def print_hello(string):
    print('Hello, ' + string + '!')

