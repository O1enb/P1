import logging
import unittest as ut


logging.basicConfig( level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(ut.TestCase):
    def test_walk(self):
        try:
            test = Runner('tname', speed=-5)
            i = 0
            while i != 10:
                test.walk()
                i += 1
            self.assertEqual(test.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            self.fail(f"Ошибка в test_walk: ValueError")


    def test_run(self):
        try:
            test = Runner(12345)
            i = 0
            while i != 10:
                test.run()
                i += 1
            self.assertEqual(test.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            self.fail(f"Ошибка в test_run: TypeError")


    def test_challenge(self):
        test1 = Runner('tname')
        test2 = Runner('tname2')
        i = 0

        while i != 10:
            test1.walk()
            test2.run()
            i += 1
        self.assertNotEqual(test1.distance, test2.distance)
        logging.info('"test_challenge" выполнен успешно')


first = Runner('Вaся', 10)
second = Runner('Вaся2', 5)
third = Runner('Арсен', 10)
t = Tournament(101, first, second)
print(t.start())
