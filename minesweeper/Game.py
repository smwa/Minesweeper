from typing import List
from random import randint

from Cell import Cell
from GameOverError import GameOverError
from InvalidNumberOfMinesError import InvalidNumberOfMinesError
from InvalidSizeError import InvalidSizeError

class Game(object):
    def __init__(self, width: int, height: int, number_of_mines: int) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.number_of_mines = number_of_mines
        if self.width < 0 or self.height < 0:
            raise InvalidSizeError()
        if self.number_of_mines > self.width * self.height or self.number_of_mines < 1:
            raise InvalidNumberOfMinesError()
        self.did_win = False
        self.did_lose = False
        self.cells = [] # type: List[Cell]
        for _ in range(self.width * self.height):
            self.cells.append(Cell())
        mines_to_go = self.number_of_mines
        while mines_to_go > 0:
            cell = self.get_cell(randint(0, self.width - 1), randint(0, self.height - 1))
            if not cell.is_mine:
                cell.is_mine = True
                mines_to_go -= 1
        for x in range(0, self.width):
            for y in range(0, self.height):
                if not self.get_cell(x, y).is_mine:
                    neighbors = 0
                    for neighbor_x in range(x - 1, x + 2):
                        for neighbor_y in range(y - 1, y + 2):
                            if not (neighbor_x == x and neighbor_y == y):
                                neighbor = self.get_cell(neighbor_x, neighbor_y)
                                if neighbor is not None and neighbor.is_mine:
                                    neighbors += 1
                    self.get_cell(x, y).number_of_neighboring_mines = neighbors
    
    def get_cell(self, x: int, y: int):
        if x >= self.width or y >= self.height:
            return None
        if x < 0 or y < 0:
            return None
        return self.cells[x + self.width * y]

    def reveal(self, x: int, y: int):
        if self.is_game_over():
            return GameOverError()
        cell = self.get_cell(x, y)
        if cell is None or cell.is_revealed or cell.is_flagged:
            return
        cell.is_revealed = True
        if cell.is_mine:
            self.did_lose = True
        else:
            self._update_game_over_states()

    def toggle_flag(self, x: int, y: int):
        if self.is_game_over():
            return GameOverError()
        cell = self.get_cell(x, y)
        if cell is not None and not cell.is_revealed:
            cell.is_flagged = not cell.is_flagged
            self._update_game_over_states()

    def _update_game_over_states(self):
        did_win_by_flags = True
        did_win_by_reveal = True
        for cell in self.cells:
            if cell.is_mine and not cell.is_flagged:
                did_win_by_flags = False
            if not cell.is_mine and not cell.is_revealed:
                did_win_by_reveal = False
        if did_win_by_flags or did_win_by_reveal:
            self.did_win = True
            return

    def is_game_over(self):
        return self.did_lose or self.did_win
