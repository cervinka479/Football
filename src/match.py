class Match:
    """Class to represent a football match."""
    def __init__(self, date: str, competition: str, home_team: str, away_team: str, home_score: str, away_score: str):
        self.date = date
        self.competition = competition
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score

    def to_dict(self) -> dict[str, str]:
        """Convert the Match object to a dictionary."""
        return {
            "date": self.date,
            "competition": self.competition,
            "home_team": self.home_team,
            "away_team": self.away_team,
            "home_score": self.home_score,
            "away_score": self.away_score,
        }