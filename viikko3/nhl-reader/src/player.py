class Player:
    def __init__(self, name, nationality, team, games, goals, assists, penalties):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.games = games
        self.goals = goals
        self.assists = assists
        self.penalties = penalties

    def __gt__(self, other):
        return (self.goals+self.assists) > (other.goals + other.assists)

    def __str__(self):
        return f'{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {(self.goals+self.assists):2}'
