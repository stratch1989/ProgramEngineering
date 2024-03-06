# Итоговый проект 
Отчет по итоговому проекту выполнил(а):
- Шайдуллин Руслан Дамирович
- ЗПИЭ-21-1

Работу проверили:
- к.э.н., доцент Панов М.А.

## Итоговый проект 

```python
import json
from datetime import date

class GetJson:
    def opene():
        with open('data.json', 'r') as file:
            data = json.load(file)
            return data
        
class WriteJSON:
    def write_json(data):
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

class Import:
    def __init__(self, item):
        self.json_data = GetJson.opene()
        self.item = item

    def json_pars(self):
        for part, general_value in self.json_data.items():
            if self.item == "history" and part == "history": return general_value
            if self.item == "statistic" and part == "statistic": return general_value
            return
        
class Statistic:
    def get_stat():
        print("\nСтатистика")
        json_data = GetJson.opene()
        all_category = dict()
        history_json = {next(iter(json_data)): json_data[next(iter(json_data))]}
        for general_value in history_json.values():
            for date_value in general_value.values():
                for key, value in date_value.items():
                    if key in all_category:
                        for current_key, sum_vaule in all_category.items():
                            if current_key == key:
                                sum_vaule += value
                                all_category.update({key: sum_vaule})
                    else:
                        all_category.update({key: value})
        # Сортировка
        sorted_data = {k: v for k, v in sorted(all_category.items(), key=lambda item: item[1], reverse=True)}
        total_sum = sum(sorted_data.values())
        print(f"Общая сумма трат: {total_sum} р.")
        for i, y in sorted_data.items():
            percentage = (y / total_sum) * 100
            print(f"Категория {i}, Сумма {y}, Процент от трат {percentage:.2f}%")
        json_data["statistic"].update(all_category)
        WriteJSON.write_json(json_data)

class HistoryParser:
    def __init__(self) -> None:
        pass

    def history_pars(self):
        importer = Import("history")
        history_json = importer.json_pars()
        return history_json
    
    def history_sort(self):
        print("\nИстория")
        history_json = self.history_pars()
        for dates, date_value in history_json.items():
                print("\n", dates)
                for key, value in date_value.items():
                    print(f"Категория: {key}. Сумма: {value} р.")


class NewCosts:
    def add_cost():
        while True:
            try:
                expenseSum = float(input("Введите потраченную сумму: "))
                break
            except ValueError:
                print("Ошибка. Нужно ввести число")
        nameExpense = input("Введите имя категории трат: ")
        today = str(date.today())
        json_data = GetJson.opene()
    
        #чтобы отделить history от остального
        history_json = {next(iter(json_data)): json_data[next(iter(json_data))]}
        for general_value in history_json.values():
            for dates, date_value in general_value.items():
                continue
        # проверяет есть ли уже такой день
        if today in general_value.keys():
            # проверяет есть ли такие же траты за сегодня
            if nameExpense in date_value:
                for key, val in date_value.items():
                    # складывает значения если уже есть имя такой траты
                    if key == nameExpense:
                        expenseSum += val
            date_value.update({nameExpense: expenseSum})
            general_value.update({dates: date_value})
        else:
            general_value.update({today: {nameExpense: expenseSum}})
        json_data["history"].update(general_value)
        WriteJSON.write_json(json_data)

class Menu:
    def choice():
        history_impoter = HistoryParser()
        print("   Меню   ")
        print("1 - для просмотра истории")
        print("2 - для просмотра статистики по категориям трат")
        print("3 - для записи новой траты")
        print("4 - выход")
        user_choice = int(input())
        if user_choice == 1:
            history_impoter.history_sort()
        elif user_choice == 2:
            Statistic.get_stat()
        elif user_choice == 3:
            NewCosts.add_cost()
        else:
            exit()
        Menu.choice()

Menu.choice()
```

```json
{
    "history": {
        "2024-03-03": {
            "rent": 20000.0,
            "food": 15000.0
        },
        "2024-03-04": {
            "gas": 3000.0,
            "food": 5000.0
        },
        "2024-03-05": {
            "internet": 1200.0,
            "phone": 70000.0,
            "education": 30000.0,
            "food": 2500.0,
            "gas": 1000.0,
            "taxi": 1500.0,
            "music": 100.0
        }
    },
    "statistic": {
        "rent": 20000.0,
        "food": 22500.0,
        "gas": 4000.0,
        "internet": 1200.0,
        "phone": 70000.0,
        "education": 30000.0,
        "taxi": 1500.0,
        "music": 100.0
    }
}
```
### Результат.
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/main/img/1.png)
![Меню](https://github.com/stratch1989/ProgramEngineering/blob/main/img/2.png)