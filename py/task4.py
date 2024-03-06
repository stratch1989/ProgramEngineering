class MyCustomException(Exception):
    pass

try:
    raise MyCustomException("Пример ошибки")
except MyCustomException as e:
    print("Обработка ошибки:", e)

def divide_numbers(a, b):
    if b == 0:
        raise MyCustomException("Деление на ноль")
    return a / b

try:
    result = divide_numbers(10, 0)
    print("Результат деления:", result)
except MyCustomException as e:
    print("Обработка ошибки:", e)