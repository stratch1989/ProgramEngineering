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