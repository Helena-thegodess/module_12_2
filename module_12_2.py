import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner("Усэйн", 10)
        self.runner2 = runner_and_tournament.Runner("Андрей", 9)
        self.runner3 = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in enumerate(cls.all_results):
            print(f"{key + 1}:{value}")

    def test1(self):
        marathon_1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        results = marathon_1.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == "Ник")

    def test2(self):
        marathon_2 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        results = marathon_2.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == "Ник")

    def test3(self):
        marathon_3 = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = marathon_3.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[3] == "Ник")

if __name__ == "__main__":
    unittest.main()