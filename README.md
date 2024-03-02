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

    def drive(self):
        if self.type == "Sport" and self.name == "Snowboarding":
            print("Тогда нужно купить экиперовку")

my_hobbie = Hobbie("Sport", "Snowboarding")
print(f'Тип хобби - {my_hobbie.type}, название хобби - {my_hobbie.name}')
my_hobbie.drive()
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_8/img/task2.png)

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

```python
f = open('task3.txt', 'r')
strings = 0
letters = 0
words = 0
for i in f.readlines():
    strings+=1
    string = i
    word = string.replace(".", "").rstrip().split(" ")
    for y in word:
        words+=1
        for letter in y:
            letters+=1
print("Input file contains:")
print(letters, "letters")
print(words, "words")
print(strings, "lines")
f.close
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_7/img/task3.png)
  
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