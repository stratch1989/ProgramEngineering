class Hobbie:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def drive(self):
        if self.type == "Sport" and self.name == "Snowboarding":
            print("Тогда нужно купить экиперовку")

my_hobbie = Hobbie("Sport", "Snowboarding")
print(f'Тип хобби - {my_hobbie.type}, название хобби - {my_hobbie.name}')
my_hobbie.drive()