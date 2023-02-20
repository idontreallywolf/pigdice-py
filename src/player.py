class Player:
    def __init__(self, name: str, score: int = 0):
        if len(name) == 0 or name.isspace():
            raise ValueError('Invalid player name.')

        self.name = name
        self.score = score
        self.temporary_score = 0
    
    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def get_name(self) -> str:
        return self.name

    def set_score(self, new_score: int) -> None:
        self.score = new_score

    def get_score(self) -> int:
        return self.score

    def add_temporary_score(self, score: int) -> None:
        """Add `score` to temporary score."""
        self.temporary_score += score

    def reset_temporary_score(self) -> None:
        """Reset temporary score."""
        self.temporary_score = 0

    def hold_score(self) -> None:
        """Increment player score by current temporary score."""
        self.score += self.temporary_score
