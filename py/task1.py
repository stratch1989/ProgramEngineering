class Hobbie:
    def __init__(self, type, name):
        self.type = type
        self.name = name

my_car = Hobbie("Sport", "Snowboarding")
print(f'Тип хобби - {my_car.type}, название хобби - {my_car.name}')