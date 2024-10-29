import math


class Figure:

    sides_count = 0

    def __init__(self, color, sides):
        if self.__is_valid_sides(sides):
            self.__sides = [sides]
        if isinstance(sides, (list, tuple)):
            if len(sides) != self.sides_count:
                self.__sides = [1] * self.sides_count
        if self.__is_valid_color(color):
            self.__color = color
        self.filled = False


    def get_color(self):
        return self.__color


    def __is_valid_color(self, color):
        for col in color:
            if not 0 <= col <= 255:
                return False
        return True


    def set_color(self, color):
        if self.__is_valid_color(color):
            self.__color = color


    def __is_valid_sides(self, *sides):
        for side in sides:
            if not (isinstance(side, int) and 0 < side):
                return False
        return True


    def get_sides(self):
        return self.__sides


    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):

    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = self.get_sides()[0] / (2*math.pi)


    def get_square(self):
        return math.pi * (self.__radius ** 2)


    def __len__(self):
        return self.get_sides()[0]


class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)


    def get_square(self):
        s = (self.__sides[0] + self.__sides[1] + self.__sides[2]) / 2
        return math.sqrt(s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2]))


class Cube(Figure):

    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = [sides] * 12


    def get_volume(self):
        return self.get_sides()[0] ** 3


    def __is_valid_sides(self, *sides):
        if not len(*sides) == 1:
            return False
        for side in sides:
            if not (isinstance(side, int) and 0 < side):
                return False
        return True


    def get_sides(self):
        return self.__sides


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130),6)


circle1.set_color((55, 66, 77))
print(circle1.get_color())
cube1.set_color((300, 70, 15))
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())