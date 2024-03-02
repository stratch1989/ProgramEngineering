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
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Hobbie:
    def __init__(self, type, name):
        self._type = type
        self.__name = name

    def buy(self):
        if self._type == "Sport" and self.__name == "Snowboarding":
            print("Тогда нужно купить экипировку")

my_hobbie = Hobbie("Sport", "Snowboarding")
print(f'Тип хобби - {my_hobbie._type}')
print('Название хобби - {my_hobbie.__name}') #Не получается воспольховаться
my_hobbie.buy()
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/Theme_8/img/task4.png)