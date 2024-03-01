# Тема 6. Базовые коллекции: словари, кортежи
Отчет по Теме #6 выполнил(а):
- Шайдуллин Руслан Дамирович
- ЗПИЭ-21-1

| Задание | Сам_раб |
| ------  | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | - |
| Задание 5 | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные вам форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте вашу задумку. Для получения начальных данных используйте input(). Результатом программы будет выведенный список и кортеж из начальных данных.

```python
form = list((input("Введите числа через пробел: ")).split(" "))

print("Список:", form)
print("Кортеж:", tuple(form))
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_6/img/task1.png)

## Самостоятельная работа №2
### Николай знает, что кортежи являются неизменяемыми, но он очень упрямый и всегда хочет доказать, что он прав. Студент решил создать функцию, которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста. Но учтите, что Николай не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией в исходном виде).

```python
tpl1 = (1, 2, 3), 1
tpl2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3
tpl3 = (2, 4, 6, 6, 4, 2), 9

def remove_element(tpl, remInd):
    modList = list(tpl)
    if remInd in tpl:
        modList.remove(remInd)
    return tuple(modList)

print("Первый кортеж:", remove_element(tpl1[0], tpl1[1]))
print("Второй кортеж:", remove_element(tpl2[0], tpl2[1]))
print("Третий кортеж:", remove_element(tpl3[0], tpl3[1]))
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_6/img/task2.png)

## Самостоятельная работа №3
### Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать победителя. Вам им нужно в этом помочь. Дана строка в виде случайной последовательности чисел от 0 до 9 (длина строки минимум 15 символов). Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию, принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел, также эти значения нужно вывести в порядке возрастания ключа.

```python
nums = input('Введите числа\n')

def add(nums): 
    dictionary = dict()
    for i in nums:
        dictionary[i] = len(nums)
    sortedDict = sorted(dictionary.items(), key=lambda item: item[0])
    print("Цифры в порядке возрастания:", dict(sortedDict).keys())
    return dictionary

def func(nums):
    dictionary = add(nums)
    print(dictionary)
func(nums)
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_6/img/task3.png)
  
## Самостоятельная работа №4
### Ваш хороший друг владеет офисом со входом по электронным картам, ему нужно чтобы вы написали программу, которая показывала в каком порядке сотрудники входили и выходили из офиса. Определение сотрудника происходит по id. Напишите функцию, которая на вход принимает кортеж и случайный элемент (id), его можно придумать самостоятельно. Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно. Если элемента нет вовсе – вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного.

```python
tuples = ['(1, 2, 3), 8)', '(1, 8, 3, 4, 8, 8, 9, 2), 8)', '(1, 2, 8, 5, 1, 2, 9), 8)']


def find_element(tple, element):
    if tple.count(element) > 0:
        start_index = tple.index(element)
        end_index = tple.index(element, start_index + 1) if tple.count(element) > 1 else ()
        return tple[start_index:end_index + 1] if end_index != () else tple[start_index:]
    else:
        return ()

for tpl in tuples:
    tple = tuple(map(int, tpl[:-4].strip('()').split(',')))
    element = int(tpl[-2:-1][0])
    new_tuple = find_element(tple, element)
    print(new_tuple)
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_6/img/task4.png)

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