# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Шайдуллин Руслан Дамирович
- ЗПИЭ-21-1

| Задание | Сам_раб |
| ------  | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Hobbie:
    def __init__(self, type, name):
        self.type = type
        self.name = name

my_hobbie = Hobbie("Sport", "Snowboarding")
print(f'Тип хобби - {my_hobbie.type}, название хобби - {my_hobbie.name}')
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_8/img/task1.png)

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Hobbie:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def buy(self):
        if self.type == "Sport" and self.name == "Snowboarding":
            print("Тогда нужно купить экипировку")

my_hobbie = Hobbie("Sport", "Snowboarding")
print(f'Тип хобби - {my_hobbie.type}, название хобби - {my_hobbie.name}')
my_hobbie.buy()
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_8/img/task2.png)

## Самостоятельная работа №3
## Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Hobbie:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def buy(self):
        print(f'Тип хобби - {self.type}, название хобби - {self.name}')
        if self.type == "Sport" and self.name == "Snowboarding":
            print("Тогда нужно купить доску")
        elif self.type == "Sport" and self.name == "Run":
            print("Тогда нужно купить кроссовки")
        
my_hobbie = Hobbie("Sport", "Run")
my_hobbie.buy()

class Equipment(Hobbie):
    def __init__(self, type, name, direction):
        super().__init__(type, name)
        self.direction = direction

    def board(self):
        if self.direction == "Freeride":
            print("Для вас хорошо подойдет доска 'BURTON FLIGHT ATTENDANT'")
        if self.direction == "Carving":
            print("Для вас хорошо подойдет доска 'Jones Freecarver 6000'")

my_equipment1 = Equipment("Sport", "Snowboarding", "Freeride")
my_equipment2 = Equipment("Sport", "Snowboarding", "Carving")
my_equipment1.buy()
my_equipment1.board()
my_equipment2.buy()
my_equipment2.board()
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_8/img/task3.png)
  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.

```python
import re

ftext = open('task4_1.txt', 'r')
fwords = open('task4_2.txt', 'r')

text = str(ftext.readline())
words = fwords.read().split()

for stopword in words:
    text = re.sub(stopword, lambda x: '*' * len(x.group()), text, flags=re.IGNORECASE)
print(text)

ftext.close
fwords.close
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_7/img/task4.png)