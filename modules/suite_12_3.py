import unittest as ut
from tests_12_3 import TournamentTest, RunnerTest


suite = ut.TestSuite()
suite.addTest(ut.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(ut.TestLoader().loadTestsFromTestCase(TournamentTest))


runner = ut.TextTestRunner(verbosity=2)
runner.run(suite)