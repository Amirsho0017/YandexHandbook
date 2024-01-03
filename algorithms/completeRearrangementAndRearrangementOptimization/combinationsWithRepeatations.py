# combination formula with repeatations: ci = (ni + ki - 1)!/(ki!(ni-1)!)
n, k = map(int, input().split())


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


kf = fact(k)
nkf = fact(n + k - 1)
nf = fact(n - 1)

print(int(nkf / (kf * nf)))
