# Тема 4. Функции и модули
Отчет по Теме #4 выполнил(а):
- Шайдуллин Руслан Дамирович
- ЗПИЭ-21-1

| Задание | Сам_раб |
| ------  | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Дайте подробный комментарий для кода, написанного ниже. Комментарий нужен для каждой строчки кода, нужно описать что она делает. Не забудь те, что функции комментируются по-особенному.

```python
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
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_4/img/task1.png)

## Самостоятельная работа №2
### Напишите программу, которая будет заменять игральную кость с 6 гранями. Если значение равно 5 или 6, то в консоль выводится «Вы победили», если значения 3 или 4, то вы рекурсивно должны вызвать эту же функцию, если значение 1 или 2, то в консоль выводится «Вы проиграли». При этом каждый вызов функции необходимо выводить в консоль значение “кубика”. Для выполнения задания необходимо использовать стандартную библиотеку random. Программу нужно написать, используя одну функцию и “точку входа”.

```python
import random

def main(digit):
    if digit == 5 or digit == 6:
        print("Вы победили")
    elif digit == 1 or digit == 2:
        print("Вы проиграли")
    else: main(random.randint(1,6))

if __name__ == '__main__':
    main(random.randint(1,6))
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_4/img/task2.png)

## Самостоятельная работа №3
### Напишите программу, на вход которой поступает значение из консоли, оно должно быть числовым и в диапазоне от 0 до 10 включительно (это необходимо учесть в программе). Если вводимое число не подходит по требованиям, то необходимо вывести оповещение об этом в консоль и остановить программу. Код должен вычислять в каком диапазоне находится полученное число. Нужно учитывать три диапазона:<br>• от 0 до 3 включительно<br>• от 3 до 6<br>• от 6 до 10 включительно<br>Результатом работы программы будет выведенный в консоль диапазон. Программа должна занимать не более 10 строчек в редакторе кода.

```python
val = int(input())
if val >= 0 and val <= 3:
    print("Первый диапозон")
elif val > 3 and val < 6:
    print("Второй диапозон")
elif val >= 6 and val < 11:
    print("Третий диапозон")
else:
    print("Число не входит ни в один диапозон")
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_3/img/task3.png)
  
## Самостоятельная работа №4
### Манипулирование строками. Напишите программу на Python, которая принимает предложение (на английском) в качестве входных данных от пользователя. Выполните следующие операции и отобразите результаты:<br>• Выведите длину предложения.<br>• Переведите предложение в нижний регистр.<br>• Подсчитайте количество гласных (a, e, i, o, u) в предложении.<br>• Замените все слова "ugly" на "beauty".<br>• Проверьте, начинается ли предложение с "The" и заканчивается ли на "end".<br>Проверьте работу программы минимум на 3 предложениях, чтобы охватить проверку всех поставленных условий.

```python
test = "The tTEST_ssiis acqwe ooo UuUu, ugly sdfwd qweqwincefvueugly end"

print("Длина текста:", len(test))
lowerText = test.lower()
print("Текст в нижнем регистре:", lowerText)
exampleLetters = "aeiou"
howManyLetters = 0
for u in exampleLetters:
    for i in lowerText:
        if i == u:
            howManyLetters += 1
    print(f"Букв {u} в тексте: {howManyLetters}")
    howManyLetters = 0
print(lowerText.replace('ugly', 'beauty'))
print(test.startswith('The') and test.endswith('end'))
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_3/img/task4.png)

## Самостоятельная работа №5
### Составьте программу, результатом которой будет данный вывод в консоль:<br>![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_3/img/5.1.png)<br>Программу нужно составить из данных фрагментов кода:<br>![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_3/img/5.2.png)<br>Строки кода можно использовать только один раз. Не обязательно использовать все строки кода.

```python
string = 'hello'
counter = 0
values = [0, 2, 4, 6, 8, 10]
while counter != 10:
    memory = string
    if counter in values:
        string = string + ' world'
    print(string)
    counter += 1
    if counter < 10:
        string = memory
        memory = ' world'
while ' world' not in string:
    if counter > 7:
        memory = ' world'
    print(string + memory)
    string = ' world'
```

### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_3/img/task5.png)