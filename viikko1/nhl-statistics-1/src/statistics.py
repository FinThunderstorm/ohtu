def sort_by_points(player):
    return player.points


class Statistics:
    def __init__(self, reader):
        reader = reader

        self._players = reader.get_players()

    def search(self, name):
        players = []
        for player in self._players:
            print(player)
            if name in player.name:
                players.append(player)
        return players if len(players) > 0 else None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top_scorers(self, how_many):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
