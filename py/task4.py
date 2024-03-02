class Hobbie:
    def __init__(self, type, name):
        self._type = type
        self.__name = name

    def buy(self):
        if self._type == "Sport" and self.__name == "Snowboarding":
            print("Тогда нужно купить экипировку")

my_hobbie = Hobbie("Sport", "Snowboarding")
print(f'Тип хобби - {my_hobbie._type}')
print(f'Название хобби - {my_hobbie.__name}') #Не получается воспольховаться
my_hobbie.buy()