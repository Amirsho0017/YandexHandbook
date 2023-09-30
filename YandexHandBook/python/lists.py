# tuple --------------------------------------------------
text = "Привет, мир!"
list_symbols = list(text)
tuple_symbols = tuple(text)
text_from_list = str(list_symbols)
print(list_symbols)
print(tuple_symbols)
print(text_from_list)


a = 1
b = 2
(a, b) = (b, a)
# можно опустить круглые скобки и записать так a, b = b, a
print(f"a = {a}, b = {b}")

# tuple кортеж -> is immutable
# example of tuple:
numbers = (1, 2, 3)
one_number = (1, )  # yes, this is correct ;)

# list --------------------------------------------------
print(sorted([5, 2, 8], reverse=False))

s = [123, 456, 7987]
s.sort(reverse=True)
print(s)

# reverse 1,3 to => 3,1
s = [123, 456, 7987]
s.reverse()

print(s)
# remove -> first el by this value
# pop -> by index
s = [1, 2, 3]
popped = s.pop()
print(popped)
print(s)

# insert -> by index
s = [1, 2, 3]
s.insert(0, 10)
print(s)

s = [1, 2, 3]
s.extend([5, 6])
print(s.copy())
# print([1, 2, 3].clear())
# append -> to add el, del -> to delete el
print([1, 2, 3, 2, 1].count(2))
print([1, 2, 3, 2, 1].index(2))
# also max, min, len
print([1, 2, 3] * 3)
print([1, 2] + [3, 4, 5])
print(4 not in [1, 2, 3])
print(1 in [1, 2, 3])

input()

# del for deleting el in list
numbers = [1, 2, 3]
del numbers[0]
print(numbers)  # [2, 3]

numbers = []
for i in range(3):
    numbers.append(int(input()))
print(numbers)


int_list = [1, 2, 10]
mixed_list = [1, 2, 'asdasd', 5.5]
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
print(numbers[1:3])
print(numbers[::-1])


# change value of el list
numbers = [10, 20, 50]
numbers[2] = 30
print(numbers)




# string ------------------------------------------------
print('rahimov amirjon'.title())  # Rahimov Amirjon

print('Rahimov,Amirjon,Barotjonovich'.split(","))  # ["Rahimov", "Amirjon", "Barotjonovich"]

print('AmirJON'.strip('JON'))  # see also rstrip and lstrip

# return str with len = 10
print("amir".ljust(10, "r"))  # see also rjust()

a = ["1", "2", "3"]
print('hello'.join(a))

# true if all is digit
print('654'.isdigit())

# true if all is letter
print('Letters'.isalpha())

# true if all is number or letter
print('amir3313'.isalnum())

# index or ValueError
print('america'.index('a'))

# find: -1 or result of count
print('Hello world'.find('a'))

# bool
print('Hello world'.endswith('a'))

s = "Hello, world!"
print(s.count("ll"))  # result: 1

s = "heLlO, World!"
s = s.capitalize()
print(s)

print("а".islower())
print("A".islower())

text = "Привет, мир!"
print(text[::-2])  # text[start:end:step]
# print(text[8:11])
# print(text[:6])
# print(text[8:])
# print(text[:])

# by index and value
text = input()
for i, letter in enumerate(text):
    print(f"{i}. {letter}")

# by values
text = input()
for letter in text:
    print(letter)

# by indexes
text = input()
for i in range(len(text)):
    print(text[i])

text = input()
print(text[len(text) - 1])
# ------ same ------
text = input()
print(text[-1])

text = input('Enter the word: ')
i = int(input('Enter index of the word: '))
if i < len(text):
    print(text[i])
else:
    print('string index out of the range')