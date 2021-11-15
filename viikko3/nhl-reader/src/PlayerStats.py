class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered_players = list(filter(lambda x: x.nationality.lower() == nationality.lower(),
                                       players))
        return sorted(filtered_players, reverse=True)
