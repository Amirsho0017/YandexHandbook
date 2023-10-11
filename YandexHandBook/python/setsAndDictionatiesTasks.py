
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
