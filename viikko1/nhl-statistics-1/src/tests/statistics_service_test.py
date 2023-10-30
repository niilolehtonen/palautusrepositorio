import unittest
from statistics_service import StatisticsService
from player import Player
from sort_by import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search(self):
        self.assertEqual(str(self.stats.search("Semenko")), f"Semenko EDM 4 + 12 = 16")
        self.assertEqual(self.stats.search("Selänne"), None)

    def test_team(self):
        edm = self.stats.team("EDM")
        self.assertEqual(len(edm), 3)
        for player in edm:
            self.assertEqual(player.team, "EDM")
    
    def test_top(self):
        top_players = self.stats.top(1)
        self.assertEqual(len(top_players), 1)
        self.assertEqual(top_players[0].name, "Gretzky")

        all_top_players = self.stats.top(5)
        self.assertEqual(len(all_top_players), 5)
        self.assertEqual(all_top_players[0].name, "Gretzky")
        self.assertEqual(all_top_players[1].name, "Lemieux")
        self.assertEqual(all_top_players[2].name, "Yzerman")
        self.assertEqual(all_top_players[3].name, "Kurri")
        self.assertEqual(all_top_players[4].name, "Semenko")

        top_goalscorer = self.stats.top(1,SortBy.GOALS)
        self.assertEqual(top_goalscorer[0].name, "Lemieux")

        top_assists = self.stats.top(2,SortBy.ASSISTS)
        self.assertEqual(top_assists[1].name, "Yzerman")

        top_points = self.stats.top(1,SortBy.POINTS)
        self.assertEqual(top_points[0].name, "Gretzky")

