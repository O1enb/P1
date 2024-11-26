import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            time.sleep(1)
            days += 1
            enemies -= self.power
            print(f'\n{self.name}, сражается {days} дней, осталось врагов {enemies}')
        print(f'\n{self.name} одержал победу спустя {days} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('\nВсе битвы закончились!')
