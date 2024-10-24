
class vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']


    def __init__(self, owner, model, en_po, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = en_po
        self.__color = color


    def get_model(self):
        print (f"Модель: {self.__model}")


    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power}")


    def get_color(self):
        print(f"Цвет: {self.__color}")


    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Владелец: {self.owner}")


    def set_color(self, new_color):
        if any(new_color.lower() == color.lower() for color in self._vehicle__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class sedan(vehicle):
    __PASSENGERS_LIMIT = 5
pass


vehicle1 = sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
