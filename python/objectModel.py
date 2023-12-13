# procedure programming

def create_car(color, consumption, tank_volume, mileage=0):
    return {
        "color": color,
        "consumption": consumption,
        "tank_volume": tank_volume,
        "reserve": tank_volume,
        "mileage": mileage,
        "engine_on": False
    }


def start_engine(car):
    if not car["engine_on"] and car["reserve"] > 0:
        car["engine_on"] = True
        return "Двигатель запущен."
    return "Двигатель уже был запущен."


def stop_engine(car):
    if car["engine_on"]:
        car["engine_on"] = False
        return "Двигатель остановлен."
    return "Двигатель уже был остановлен."


def drive(car, distance):
    if not car["engine_on"]:
        return "Двигатель не запущен."
    if car["reserve"] / car["consumption"] * 100 < distance:
        return "Малый запас топлива."
    car["mileage"] += distance
    car["reserve"] -= distance / 100 * car["consumption"]
    return f"Проехали {distance} км. Остаток топлива: {car['reserve']} л."


def refuel(car):
    car["reserve"] = car["tank_volume"]


def get_mileage(car):
    return f"Пробег {car['mileage']} км."


def get_reserve(car):
    return f"Запас топлива {car['reserve']} л."


car_1 = create_car(color="black", consumption=10, tank_volume=55)

print(start_engine(car_1))
print(drive(car_1, 100))
print(drive(car_1, 100))
print(drive(car_1, 100))
print(drive(car_1, 300))
print(get_mileage(car_1))
print(get_reserve(car_1))
print(stop_engine(car_1))
print(drive(car_1, 100))


# OOP - object-oriented-programming
class Car:

    def __init__(self, color, consumption, tank_volume, mileage=0):
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен."
        return "Двигатель уже был запущен."

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен."
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас топлива."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."

    def refuel(self):
        self.reserve = self.tank_volume

    def get_mileage(self):
        return self.mileage

    def get_reserve(self):
        return self.reserve


car_1 = Car(color="black", consumption=10, tank_volume=55)
print(car_1.start_engine())
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(300))
print(f"Пробег {car_1.get_mileage()} км.")
print(f"Запас топлива {car_1.get_reserve()} л.")
print(car_1.stop_engine())
print(car_1.drive(100))
