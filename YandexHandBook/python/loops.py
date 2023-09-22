n = int(input("Введите количество чисел: "))
for i in range(n, -1, -1):
    print(i)

n = int(input("Введите количество чисел: "))
for i in range(n):
    print(i)

# range(start, end, step)
while (name := input('Enter name: ')) != "stop":
    print(name)
print('bye')

passwd = '132'
while input('Enter Password: ') != passwd:
    pass
print('Welcome')

name = input('enter name: ')
while name != "stop":
    name = input('Enter name: ')
print('bye')
