def validate_string_input(value, field_name):
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")


def validate_username(username):
    validate_string_input(username, "Username")


def validate_first_name(first_name):
    validate_string_input(first_name, "First Name")


def validate_last_name(last_name):
    validate_string_input(last_name, "Last Name")


def user_validation(**kwargs):
    fields_order = ["last_name", "first_name", "username"]

    for key, val in kwargs.items():
        if key not in fields_order:
            raise KeyError(f"Вызвано исключение KeyError")
        if key == "last_name":
            validate_last_name(kwargs[val])
        elif key == "first_name":
            validate_first_name(kwargs[val])
        elif key == "username":
            validate_username(kwargs[val])

    return kwargs


print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45", password="123456"))


def only_positive_even_sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both parameters must be integers")

    if a <= 0 or b <= 0 or a % 2 != 0 or b % 2 != 0:
        raise ValueError("Both parameters must be positive even numbers")

    return a + b


def func(a, b):
    return a * b


try:
    func('a', {'hello': 'world'})
except Exception:
    print(Exception('Ура! Ошибка!'))
else:
    print("Повезёт в следующий раз!")


def func():
    x = int('Hello, world!')


try:
    func()
except ValueError:
    print('ValueError')
except TypeError:
    print("TypeError")
except SystemError:
    print('SystemError')
else:
    print('No Exceptions')
