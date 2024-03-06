class MyCustomException(Exception):
    pass

def check_positive_number(number):
    if number < 0:
        raise MyCustomException("Отрицательные числа не допускаются")

try:
    check_positive_number(-5)
except MyCustomException as e:
    print("Ошибка:", e)

def process_data(data):
    if not data:
        raise MyCustomException("Пустые данные обнаружены")

try:
    process_data([])
except MyCustomException as e:
    print("Ошибка:", e)
