class Tomato:
    states = ['отсутствует', 'цветение', 'зеленый', 'красный']

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]

    def grow(self):
        self._state = Tomato.states[(Tomato.states.index(self._state) + 1) % len(Tomato.states)]

    def is_ripe(self):
        return self._state == 'красный'
    
class TomatoBush:
    def __init__(self, sum_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(sum_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)
    
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f'собрали урожай, садовник - {self.name}')
            self._plant.give_away_all()
        else:
            print('не все томаты красные')

    @staticmethod
    def knowledge_base():
        print('справка')


Gardener.knowledge_base()

bush = TomatoBush(5)
gardener = Gardener('Олег', bush)

for _ in range(10):
    gardener.work()

gardener.harvest()

for _ in range(5):
    gardener.work()

gardener.harvest()