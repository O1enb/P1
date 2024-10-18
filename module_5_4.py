

class houses:

    house_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(houses, cls).__new__(cls)
        cls.house_history.append(kwargs.get('name'))
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = houses(name = 'ЖК Эльбрус', number_of_floors = 10)
print(houses.house_history)
h2 = houses(name = 'ЖК Акация', number_of_floors = 20)
print(houses.house_history)
h3 = houses(name = 'ЖК Матрёшки', number_of_floors = 20)
print(houses.house_history)

del h2
del h3

print(houses.house_history)
