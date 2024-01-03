# P(n) = n! (factorial)

number = int(input())
result = 1
for i in range(1, number + 1):
    result *= i

print(result)
