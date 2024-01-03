# combination formula: ci = ni!/(ki!(ni-ki)!)
n, k = map(int, input().split())


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


nf = fact(n)
kf = fact(k)
diff = fact(n - k)

print(int(nf / (kf * diff)))
