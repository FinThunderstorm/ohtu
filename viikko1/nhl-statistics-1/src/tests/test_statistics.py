import unittest
from statistics import Statistics
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_statistics_initializes(self):
        self.assertIsNotNone(self.statistics)
        self.assertIsInstance(self.statistics, Statistics)

    def test_search_finds_with_fullname(self):
        kurri = self.statistics.search('Kurri')
        self.assertEqual(str(kurri), str(Player("Kurri", "EDM", 37, 53)))

    def test_search_returns_none_if_no_results(self):
        no_players = self.statistics.search('Kapanen')
        self.assertIsNone(no_players)

    def test_team_finds_correct(self):
        team = self.statistics.team('EDM')
        self.assertEqual(len(team), 3)
        for player in team:
            self.assertEqual(player.team, 'EDM')

    def test_team_no_team_is_empty(self):
        team = self.statistics.team('KAL')
        self.assertEqual(len(team), 0)

    def test_team_find_also_one(self):
        team = self.statistics.team('DET')
        self.assertEqual(len(team), 1)
        self.assertEqual(str(team[0]), str(Player("Yzerman", "DET", 42, 56)))

    def test_top_scorers_returns_right_top_three(self):
        top_players = self.statistics.top_scorers(3)
        top_three = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56)
        ]
        self.assertEqual(len(top_players), 3)
        for i in range(3):
            self.assertEqual(str(top_players[i]), str(top_three[i]))

    def test_top_scorers_returns_only_players_existing(self):
        top_players = self.statistics.top_scorers(10**5)
        self.assertEqual(len(top_players), 5)

    def test_top_scorers_returns_nothing_negative_amount(self):
        top_players = self.statistics.top_scorers(-5)
        self.assertEqual(len(top_players), 0)
