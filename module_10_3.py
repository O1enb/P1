import threading
import random
import time


class Bank:
    def __init__(self,) :
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for _ in range(100):
            added = random.randint(50, 500)
            self.balance += added
            print(f'Пополнение: {added}, Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)


    def take(self):
        for _ in range(100):
            taken = random.randint(50, 500)
            print(f'Запрос на: {taken}')
            if taken <= self.balance:
                self.balance -= taken
                print(f'Снятие: {taken}, Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'\nИтоговый баланс: {bk.balance}')