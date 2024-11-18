import io
import random


first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x,y: x == y, first, second))
print(result)

def get_advanced_writer(file_name):
    file = open(file_name, 'w', encoding="utf-8")
    def write_everything(*data_set):
        for data in data_set:
            file.write(f'{data}\n')
        file.close()
    return write_everything


write = get_advanced_writer('test_file.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words


    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())