# dict(dictionaries) ----------------

# operators
# len, del d[key], dict.clear(), dict.copy(), dict.get(key, default) -> if key not exists returns default
# dict.items() -> returns iterable object (keys, values)
# dict.keys() -> return iterable object (keys)
# dict.values() -> return iterable object (values)
# dict.pop(key, default) -> return iterable object (keys)

# value of keys in dict can be any data type
countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
for country in countries_and_capitals:
    print(f"У страны {country} столица — {countries_and_capitals[country]}.")

countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
if "Сербия" in countries_and_capitals:
    print(countries_and_capitals["Сербия"])
else:
    print("Страна пока не добавлена в словарь")

d = {"key": "old_value"}
d["key"] = "new_value"
print(d["key"])

countries_and_capitals = {"Россия": "Москва", "США": "Вашингтон", "Франция": "Париж"}
countries_and_capitals["Сербия"] = "Белград"
print(countries_and_capitals["Франция"])
print(countries_and_capitals["Сербия"])

countries_and_capitals = [("Россия", "Москва"), ("США", "Вашингтон"), ("Франция", "Париж")]
print(countries_and_capitals)

# -------- sets is changeable
set1 = set()
set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)
set1.remove(1)
set1.discard(1)  # delete if exists
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)
s1 = {1, 2, 3}
s2 = {3, 4, 5, 1, 2}

# superset
print(s1 >= s2)

# subset
print(s1 <= s2)

# check is equal
print(s1 == s2)

# symmetric difference or ^
print(s1 ^ s2)

# difference or -
print(s1 - s2)
print(s2 - s1)


# intersection or &
s_intersection = s1 & s2
print(s_intersection)

# union(merge unique), union() or |
s_union = s1 | s2
print(s_union)  # {1, 2, 3, 4, 5}
s_union = s1.union(s2)
print(s_union)  # {1, 2, 3, 4, 5}

# can iterate
# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# for letter in vowels:
    # print(letter)

# can check by "in" operator
vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
letter = input("Введите букву русского алфавита: ")
if letter.lower() in vowels:
    print("Гласная буква")
else:
    print("Согласная буква")

# no indexes in sets, all elements is unique
word = "Hello world"
letters = set(word)
print(letters)  # different every time
print(letters)  # different every time


vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}

empty_set = set()
print(f"Длина пустого множества равна {len(empty_set)}.")  # Длина пустого множества равна 0.

