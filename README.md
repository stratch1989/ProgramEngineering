# Тема 3. Операторы, условия, циклы
Отчет по Теме #3 выполнил(а):
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
### Напишите программу, которая преобразует 1 в 31. Для выполнения поставленной задачи необходимо обязательно и только один раз использовать:<br>• Цикл for<br>• *= 5<br>• += 1<br>Никаких других действий или циклов использовать нельзя.

```python
var = 1

for i in range(2):
    var *= 5
    var += 1

print(var)
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_3/img/task_1.png)

## Самостоятельная работа №2
### Напишите программу, которая фразу «Hello World» выводит в обратном порядке, и каждая буква находится в одной строке консоли. При этом необходимо обязательно использовать любой цикл, а также программа должна занимать не более 3 строк в редакторе кода.

```python
var = "Hello world"
for i in var[::-1]:
    print(i)
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_3/img/task2.png)

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
### Составьте программу, результатом которой будет данный вывод в консоль:<br>![Меню](https://github.com/segamega-drive/software_engineering/blob/Theme_3/img/5.1.png)<br>Программу нужно составить из данных фрагментов кода:<br>![Меню](https://github.com/segamega-drive/software_engineering/blob/Theme_3/img/5.2.png)<br>Строки кода можно использовать только один раз. Не обязательно использовать все строки кода.

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