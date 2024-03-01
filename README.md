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
| Задание 5 | + |

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
### Преподаватель по математике придумал странную задачку. У вас есть три списка с элементами, каждый элемент которых – длина стороны треугольника, ваша задача найти площади двух треугольников, составленные из максимальных и минимальных элементов полученных списков. Результатом выполнения задачи будет: листинг кода, и вывод в консоль, в котором будут указаны два этих значения. Три списка:<br>one = [12, 25, 3, 48, 71]<br>two = [5, 18, 40, 62, 98]<br>three = [4, 21, 37, 56, 84]

```python
from math import sqrt 
list1 = [12, 25, 3, 48, 71]
list2 = [5, 18, 40, 62, 98]
list3 = [4, 21, 37, 56, 84]

def calculatingArea(a, b, c):
    p = (a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))

print("Самый большой треугольник:", calculatingArea(max(list1), max(list2), max(list3)))
print("Самый маленький треугольник:", calculatingArea(min(list1), min(list2), min(list3)))
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_5/img/task3.png)
  
## Самостоятельная работа №4
### Никто не любит получать плохие оценки, поэтому Борис решил это исправить. Допустим, что все оценки студента за семестр хранятся в одном списке. Ваша задача удалить из этого списка все двойки, а все тройки заменить на четверки. Списки оценок (проверить работу программы на всех трех вариантах):<br>[2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]<br>[4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]<br>[5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]<br>Результатом выполнения задачи будет: листинг кода, и вывод в консоль, в котором будут три обновленных массива.

```python
list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def modifyList(list):
    for _ in range(list.count(2)):
        list.remove(2)
    for index, item in enumerate(list):
        if item == 3:
            list[index] = 4
    return list

print(modifyList(list1))
print(modifyList(list2))
print(modifyList(list3))
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_5/img/task4.png)

## Самостоятельная работа №5
### Вам предоставлены списки натуральных чисел, из них необходимо сформировать множества. При этом следует соблюдать это правило: если какое-либо число повторяется, то преобразовать его в строку по следующему образцу: например, если число 4 повторяется 3 раза, то в множестве будет следующая запись: само число 4, строка «44», строка «444». Множества для теста:<br>list_1 = [1, 1, 3, 3, 1]<br>list_2 = [5, 5, 5, 5, 5, 5, 5]<br>list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]<br>Результаты вывода (порядок может отличаться, поскольку мы работаем с set()):<br>{'11', 1, 3, '33', '111'}<br>{5, '5555', '555555', '55555', '555', '55', '5555555'}<br>{'11', 1, 3, 2, 5, 6, '222222', '222', 7, '2222', '22222', '22'}

```python
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


def listsToSet(list):
    setFromList = set(list)
    sortSet = set()
    for i in setFromList:
        countDigit = list.count(i)
        sortSet.add(i)
        for y in range(2, countDigit+1):
            sortSet.add(str(i)*y)
    print(sortSet)
    
listsToSet(list_1)
listsToSet(list_2)
listsToSet(list_3)
```

### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_5/img/task5.png)