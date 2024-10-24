
class animal:

    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed


    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class plant:
    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible


class mammal(animal):
    pass

class predator(animal):
    pass

class flower(plant):
    pass

class fruit(plant):
    def __init__(self, name):
        self.name = name
        self.edible = True


a1 = predator('Волк с Уолл-Стрит')
a2 = mammal('Хатико')
p1 = flower('Цветик семицветик')
p2 = fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
