
class horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frr'


    def run(self, dx):
        self.x_distance += dx


class eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'i train, eat, sleep, and repeat'


    def fly(self, dy):
        self.y_distance += dy


class pegasus(horse, eagle):

    def __init__(self):
        super().__init__()
        eagle.__init__(self)


    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)


    def get_pos(self):
        return (self.x_distance, self.y_distance)


    def voice(self):
        print(f'{self.sound}')


p1 = pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()