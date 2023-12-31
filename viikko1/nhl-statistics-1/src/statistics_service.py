from sort_by import SortBy

class StatisticsService:
    def __init__(self,reader):
        self._reader = reader

        self._players = self._reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=None):

        sort_methods = {
            SortBy.POINTS: lambda player: player.points,
            SortBy.GOALS: lambda player: player.goals,
            SortBy.ASSISTS: lambda player: player.assists,
        }

        if sort_by in sort_methods:
            sort_method = sort_methods[sort_by]
        else:
            sort_method = lambda player: player.points


        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_method
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
