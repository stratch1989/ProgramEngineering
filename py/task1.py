# Из модуля datetime импортируем класс datetime для создания объекта из текущих даты и времени
from datetime import datetime

# Из модуля math импортируем функцию sqrt для вычисления квадратного корня
from math import sqrt


def main(**kwargs):
    '''
    Вычисляет квадратный корень из суммы квадратов значений.
    **kwargs принимает переменное количество аргументов типа данных словарь со значениями в виде списка чисел.
    return выводит результат.
    '''
    for key in kwargs.items():
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        print(result)


if __name__ == '__main__':  # Условие начала выполнения если не вызывается из другого модуля, а запускается напрямую
    start_time = datetime.now()  # Создание объекта времени начала выполнения программы
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15])  # Вызов функции с параметрами — списками чисел

# Подсчёт времени выполнения программы, для этого из текущего времени вычитается время начала выполнения
time_costs = datetime.now() - start_time

print(f"Время выполнения программы {time_costs}")  # Вывод времени, за которое была выполнена программа