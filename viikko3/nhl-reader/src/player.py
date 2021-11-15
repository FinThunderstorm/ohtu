class Player:
    def __init__(self, name, nationality, team, games, goals, assists, penalties):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.games = games
        self.goals = goals
        self.assists = assists
        self.penalties = penalties

    def __str__(self):
        return f'{self.name} ({self.nationality})\n - Team: {self.team}\n - Games: {self.games}\n - Goals: {self.goals}\n - Assists: {self.assists}\n - Penalties: {self.penalties} minutes\n'
