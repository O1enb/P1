import unittest as ut


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(ut.TestCase):
    def test_walk(self):
        test = Runner('tname')
        i = 0
        while i != 10:
            test.walk()
            i += 1
        self.assertEqual(test.distance, 50)


    def test_run(self):
        test = Runner('tname')
        i = 0
        while i != 10:
            test.run()
            i += 1
        self.assertEqual(test.distance, 101)


    def test_challenge(self):
        test1 = Runner('tname')
        test2 = Runner('tname2')
        i = 0

        while i != 10:
            test1.walk()
            test2.run()
            i += 1

        self.assertNotEqual(test1.distance, test2.distance)