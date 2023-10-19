# P
li = []
se = set()
while (text := input()) != '':
    things = text.split(' ')
    for key, val in enumerate(things):
        if 'зайка' == val:
            if key != 0:
                se.add(things[key - 1])
            if key + 1 != len(things):
                se.add(things[key + 1])
print('\n'.join(se))

# N
products = set()
for _ in range(int(input())):
    products.add(input())
foods_with_ingredients = {}
for _ in range(int(input())):
    name_of_food = input()
    foods_with_ingredients[name_of_food] = set()
    for _ in range(int(input())):
        foods_with_ingredients[name_of_food].add(input())
res = []
for key, val in foods_with_ingredients.items():
    if val <= products:
        res.append(key)

res = sorted(res)
if len(res) == 0:
    print('Готовить нечего')
else:
    print('\n'.join(res))

# M
quantity_of_foods = int(input())
food_counter = 0
list_of_foods = set()
list_of_prepared_foods = set()
while food_counter < quantity_of_foods:
    food_counter += 1
    list_of_foods.add(input())

days = int(input())
day_counter = 0
while day_counter < days:
    day_counter += 1
    quantity_of_prepared_foods = int(input())
    quantity_of_prepared_foods_counter = 0
    while quantity_of_prepared_foods_counter < quantity_of_prepared_foods:
        quantity_of_prepared_foods_counter += 1
        list_of_prepared_foods.add(input())
res = sorted(list_of_foods - list_of_prepared_foods)
if len(res) == 0:
    print('Готовить нечего')
else:
    print('\n'.join(res))

# L
num = int(input())
di = {}
q = 0
li = []
for i in range(num):
    text = input()
    if text in di:
        di[text] += 1
    else:
        di[text] = 1

for key, val in di.items():
    if val > 1:
        li.append(f"{key} - {val}")
        q += 1

li = sorted(li)
if q == 0:
    print('Однофамильцев нет')
else:
    print('\n'.join(li))

# K
num = int(input())
di = dict()
q = 0
for i in range(num):
    text = input()
    if text not in di:
        di[text] = 1
    else:
        di[text] += 1

for i in di.values():
    if i > 1:
        q += i

print(q)

# J
d = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Э": "E",
    "Ю": "IU",
    "Ь": "",
    "Ъ": "",
    "Я": "IA",
}

text = input()
result = ""

for letter in text:
    if letter.upper() in d:
        if letter.isupper():
            print(letter)
            result += d[letter.upper()].capitalize()
            print(result)
        else:
            result += d[letter.upper()].lower()
    else:
        result += letter

print(result)


# I
di = dict()
while (text := input()) != '':
    for i in text.split(' '):
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1

for key, val in di.items():
    print(key, val)

# H
num = int(input())
names = dict()

for i in range(num):
    text = input().split(' ')
    names[text[0]] = text[1:]

type2 = input()
lis = []
for key, val in names.items():
    if type2 in val:
        lis.append(key)

if len(lis) == 0:
    print('Таких нет')
else:
    print('\n'.join(sorted(lis)))

# G
dic = {'A': '.-', 'B': '-...', 'C': '-.-.',
       'D': '-..', 'E': '.', 'F': '..-.',
       'G': '--.', 'H': '....', 'I': '..',
       'J': '.---', 'K': '-.-', 'L': '.-..',
       'M': '--', 'N': '-.', 'O': '---',
       'P': '.--.', 'Q': '--.-', 'R': '.-.',
       'S': '...', 'T': '-', 'U': '..-',
       'V': '...-', 'W': '.--', 'X': '-..-',
       'Y': '-.--', 'Z': '--..',
       '0': '-----', '1': '.----', '2': '..---',
       '3': '...--', '4': '....-', '5': '.....',
       '6': '-....', '7': '--...', '8': '---..',
       '9': '----.'}

text = input()
s = ''
for index, i in enumerate(text):
    print(i)
    if i == ' ':
        s = ''
    else:
        s += dic[i.upper()] + ' '
        if index + 1 == len(text):
            print(s)

# F
num1 = int(input())
num2 = int(input())
set1 = set()
set2 = set()

k = 0
while k < num1 + num2:
    k += 1
    a = input()
    if a not in set1:
        set1.add(a)
    else:
        set2.add(a)

if len(set1 ^ set2) == 0:
    print('Таких нет')
else:
    print('\n'.join(sorted(set1 ^ set2)))

# E
num1 = int(input())
num2 = int(input())
set1 = set()
set2 = set()

k = 0
while k < num1 + num2:
    k += 1
    a = input()
    if a not in set1:
        set1.add(a)
    else:
        set2.add(a)

if len(set1 ^ set2) == 0:
    print('Таких нет')
else:
    print(len(set1 ^ set2))

# D
num1 = int(input())
num2 = int(input())
set1 = set()
set2 = set()

k = 0
while k < num1:
    k += 1
    set1.add(input())

k = 0
while k < num2:
    k += 1
    set2.add(input())

if len(set1 & set2) == 0:
    print('Таких нет')
else:
    print(len(set1 & set2))

# C
k = 0
num = int(input())
set1 = set()
while k < num:
    k += 1
    for i in input().split(' '):
        set1.add(i)
print('\n'.join(set1))

# B
print(''.join(set(input()) & set(input())))

# A
text = input()
text = set(text)
print(''.join(text))
