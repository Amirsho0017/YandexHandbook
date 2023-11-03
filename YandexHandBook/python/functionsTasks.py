# gdc 2.0
def gcd(*args):
    if len(args) == 1:
        return args[0]
    if sum(args) / len(args) == args[0]:
        return args[0]
    else:
        length = len(args)
        a = args[0]
        for i in range(1, length):
            b = args[i]
            while b != 0:
                a, b = b, a % b
    return a


print(gcd(36, 48, 156, 100500))
# MatrixGenerator
def make_matrix(size, value=0):
    if isinstance(size, int):
        return [[value] * size for _ in range(size)]
    else:
        return [[value] * size[0] for _ in range(size[1])]


print(make_matrix((4, 2), 1))
print(make_matrix(3))


# ListGenerator
def make_list(length, value=0):
    return [value for _ in range(length)]


# print(make_list(5, 1))


# I
def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True


# G
def can_eat(first_pos, second_pos) -> bool:
    check_1 = ((first_pos[0] + 2 == second_pos[0]) and (first_pos[1] + 1 == second_pos[1]))
    check_2 = ((first_pos[0] - 2 == second_pos[0]) and (first_pos[1] - 1 == second_pos[1]))
    check_3 = ((first_pos[0] + 1 == second_pos[0]) and (first_pos[1] + 2 == second_pos[1]))
    check_4 = ((first_pos[0] - 1 == second_pos[0]) and (first_pos[1] - 2 == second_pos[1]))
    check_5 = ((first_pos[0] - 1 == second_pos[0]) and (first_pos[1] + 2 == second_pos[1]))
    check_6 = ((first_pos[0] + 1 == second_pos[0]) and (first_pos[1] - 2 == second_pos[1]))
    check_7 = ((first_pos[0] - 2 == second_pos[0]) and (first_pos[1] + 1 == second_pos[1]))
    check_8 = ((first_pos[0] + 2 == second_pos[0]) and (first_pos[1] - 1 == second_pos[1]))

    if check_1 or check_2 or check_3 or check_4 or check_5 or check_6 or check_7 or check_8:
        return True
    else:
        return False


def can_eat(first_pos, second_pos) -> bool:
    move_offsets = [(2, 1), (-2, -1), (1, 2), (-1, -2), (-1, 2), (1, -2), (-2, 1), (2, -1)]
    return any((
                       first_pos[0] + offset[0] == second_pos[0]
                       and first_pos[1] + offset[1] == second_pos[1]
               ) for offset in move_offsets)


# print(can_eat((1, 1), (3, 2)))


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
