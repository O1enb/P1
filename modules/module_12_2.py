import unittest as ut


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class TournamentTest(ut.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runners = [
        Runner('Usain', 10),
        Runner('Andrei', 9),
        Runner('Nick', 3)
        ]

    @classmethod
    def tearDownClass(cls):
        for test_name, test_results in cls.all_results.items():
            print('')
            for place, runner in sorted(test_results.items()):
                print(f'{runner}: {place}', end=' ', flush=True)


    def test1(self):
        participants = [self.runners[0], self.runners[2]]
        tournament = Tournament(90, *participants)
        result = tournament.start()
        self.__class__.all_results['test1'] = result
        self.assertTrue(result[max(result.keys())].name == 'Nick')


    def test2(self):
        participants = [self.runners[1], self.runners[2]]
        tournament = Tournament(90, *participants)
        result = tournament.start()
        self.__class__.all_results['test2'] = result
        self.assertTrue(result[max(result.keys())].name == 'Nick')


    def test3(self):
        tournament = Tournament(90, *self.runners)
        result = tournament.start()
        self.__class__.all_results['test3'] = result
        self.assertTrue(result[max(result.keys())].name == 'Nick')
