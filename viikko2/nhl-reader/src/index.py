import requests
from player import Player

class PlayerReader:

    def __init__(self,url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players

class PlayerStats:
    
    def __init__(self,reader):
        self.reader = reader

    def top_scorers_by_nationality(self,nationality):
        players_by_nation = []
        players = self.reader.get_players()
        sorted_players = sorted(players, key=lambda x: x.points, reverse=True)
        for player in sorted_players:
            if player.nation == nationality:
                players_by_nation.append(player)
        return players_by_nation

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
