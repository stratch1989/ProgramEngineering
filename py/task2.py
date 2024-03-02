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