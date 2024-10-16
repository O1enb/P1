

class house:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            print(new_floor)


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f"Название: {self.name}, Кол-во этажей: {self.number_of_floors}"


    def __eq__(self, other):
        if isinstance(other, house):
            return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        if isinstance(other, house):
            return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
        if isinstance(other, house):
            return self.number_of_floors <= other.number_of_floors


    def __gt__(self, other):
        if isinstance(other, house):
            return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
        if isinstance(other, house):
            return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        if isinstance(other, house):
            return self.number_of_floors != other.number_of_floors


    def __add__(self, value):
        if isinstance(value, (int, float)):
            self.number_of_floors = self.number_of_floors + value
            return self


    def __radd__(self, value):
        if isinstance(value, (int, float)):
            self.number_of_floors = value + self.number_of_floors
            return self


    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.number_of_floors += value
            return self


h1 = house('ЖК Эльбрус', 10)
h2 = house('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)




