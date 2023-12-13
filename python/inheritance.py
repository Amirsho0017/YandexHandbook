class Pencil:

    def __init__(self, color="серый"):
        self.color = color

    def draw_picture(self):
        return f"Нарисован рисунок цветом '{self.color}'."


class Pen(Pencil):

    def __init__(self, color, pen_type):
        super().__init__(color)
        self.pen_type = pen_type

    def sign_document(self):
        if self.color not in ("синий", "чёрный", "фиолетовый"):
            return f"Ручкой цвета '{self.color}' нельзя подписать документ."
        elif self.pen_type == "гелевая":
            return f"Ручкой типа '{self.pen_type}' нельзя подписать документ."
        return f"Подписан документ."


blue_ball_pen = Pen(color="синий", pen_type="шариковая")
print(blue_ball_pen.draw_picture())
print(blue_ball_pen.sign_document())
blue_gel_pen = Pen(color="синий", pen_type="гелевая")
print(blue_gel_pen.draw_picture())
print(blue_gel_pen.sign_document())


class GreetingFormal:

    def __init__(self):
        self.formal_greeting = "Добрый день,"

    def greet_formal(self, name):
        return f"{self.formal_greeting} {name}!"


class GreetingInformal:

    def __init__(self):
        self.informal_greeting = "Привет,"

    def greet_informal(self, name):
        return f"{self.informal_greeting} {name}!"


class GreetingMix(GreetingFormal, GreetingInformal):

    def __init__(self):
        GreetingFormal.__init__(self)
        GreetingInformal.__init__(self)


mixed_greeting = GreetingMix()
print(mixed_greeting.greet_formal("Пользователь"))
print(mixed_greeting.greet_informal("Пользователь"))