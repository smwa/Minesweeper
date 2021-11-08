class Cell(object):
    def __init__(self) -> None:
        super().__init__()
        self.is_mine = False
        self.number_of_neighboring_mines = 0
        self.is_revealed = False
        self.is_flagged = False
