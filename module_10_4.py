import threading
import random
import time
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name


    def run(self):
        time.sleep(random.randint(3,10))


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables


    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} Сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')


    def serve_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} завершил(-а) приём пищи и ушёл. Стол {table.number} свободен.')
                        table.guest = None
                        if not self.queue.empty():
                            table.guest = self.queue.get()
                            table.guest.start()
                            print(f'{table.guest.name} Вышел(-ла) из очереди и сел(-а) за стол {table.number}')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.serve_guests()