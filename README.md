# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
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
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
f = open('task1.txt', 'r')
text = str(f.readlines()).replace(',','').replace('.','').replace('\\n','').replace("'",'').lower()
text1 = list(text.split(' '))
example = 0
word = ""
hWord = 0
for i in text1:
    for y in text1:
        if i == y:
            example += 1
        if example > hWord:
            hWord = example
            word = i
    example = 0
print("Всего слов:", len(text1))
print(f'Самое часто встречаемое слово - "{word}", оно встречается {hWord} раз')
f.close
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_7/img/task1.png)

## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
#Востанавливаем данные из файла по последним тратам
def readLastExpenses():
    f = open('task2.txt', 'r')
    lastExpenses_str = str(f.readlines()).replace("[", "").replace("]", "").replace("'", "")
    lastExpenses_partitions = lastExpenses_str.split("|")
    f.close

    lastExpenses = dict()
    for i in range(len(lastExpenses_partitions)):
        lastExpenses_topics = lastExpenses_partitions[i].split("+")
        lastExpenses.update({lastExpenses_topics[0]: lastExpenses_topics[1]})
    return lastExpenses

lastExpenses = readLastExpenses()

#Получение новых данных
expenseSum = float(input("Введите потраченную сумму: "))
nameExpense = input("Введите имя категории трат: ")

#Запись новых данных
lastExpenses.update({nameExpense: expenseSum})
with open('task2.txt', 'a') as f:
    f.write(f'|{nameExpense}+{expenseSum}')
    f.close

print(lastExpenses)
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_7/img/task2.png)

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