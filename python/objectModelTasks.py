class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        return round(((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5, 2)


point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))


class RedButton:
    def __init__(self):
        self.counter = 0

    def click(self):
        self.counter += 1
        print('Тревога!')

    def count(self):
        return self.counter


first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())


class Programmer:
    levels = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.time = 0
        self.salary = self.levels[self.level]
        self.earned_money = 0

    def work(self, time):
        self.time += time
        self.earned_money += self.salary * time

    def rise(self):
        if self.level == "Junior":
            self.level = 'Middle'
            self.salary = self.levels[self.level]
        elif self.level == "Middle":
            self.level = 'Senior'
            self.salary = self.levels[self.level]
        else:
            self.salary += 1

    def info(self):
        return f"{self.name} {self.time}ч. {self.earned_money}тгр."


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
