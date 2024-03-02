class Hobbie:
    def __init__(self, type, name):
        self.type = type
        self.name = name

my_hobbie = Hobbie("Sport", "Snowboarding")
print(f'Тип хобби - {my_hobbie.type}, название хобби - {my_hobbie.name}')