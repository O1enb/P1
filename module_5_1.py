

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            print(new_floor)


house1 = House('ЖК Эльбрус', 30)
house2 = House('Домик в деревне', 2)

house1.go_to(5)
house1.go_to(10)
house2.go_to(1)
house2.go_to(5)
