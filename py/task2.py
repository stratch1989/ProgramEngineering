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