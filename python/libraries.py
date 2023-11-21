import itertools
from itertools import count
from itertools import cycle
from itertools import repeat
from itertools import accumulate
from itertools import chain
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

for index, value in enumerate("ABC", 1):
    print(index, value)

values = list(combinations_with_replacement("АБВ", 2))
print(values)

values = list(combinations("АБВ", 1))
print(values)

values = list(permutations("АБВ"))
print(values)

values = list(product([1, 2, 3], "АБВГ", repeat=2))
print(values)

values = list(product([1, 2, 3], "АБВГ"))
print(values)

values = list(chain.from_iterable(["АБВ", "ГДЕЁ", "ЖЗИЙК"]))
print(values)

values = list(chain("АБВ", "ГДЕЁ", "ЖЗИЙК"))
print(values)

for value in accumulate([1, 2, 3, 4, 5]):
    print(value)


result = list(repeat("ABC", 5))
print(result)

max_len = 10
s = ""
for letter in cycle("ABC"):
    if len(s) < 10:
        s += letter
    else:
        break
print(s)


for value in count(0, 0.1):
    if value <= 1:
        print(round(value, 1))
    else:
        break


print(itertools.product("ABC", repeat=2))
print(list(product("ABC", repeat=2)))

print(list(zip("ABC", [1, 2, 3])))
print(list(zip("ABCDE", [1, 2, 3])))
print(list(zip("ABCDE", [1, 2, 3], strict=True)))
