class InvalidMove(Exception):
    pass


class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:

    _WIN_LINES = (["A1", 'A2', "A3"], ["B1", "B2", "B3"],
                 ["C1", "C2", "C3"], ["A1", "B1", "C1"], ["A2", "B2", "C2"],
                 ["A3", "B3", "C3"], ["A1", "B2", "C3"], ["A3", "B2", "C1"])
    _CELLS = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')

    def __init__(self):
            self._board = {position: ' ' for position in self._CELLS}
            self._previous = None
            self._winner = None

    def update_winner(self):
        if not self._winner:
            for line in self._WIN_LINES:
                if (self._board[line[0]] == self._board[line[1]] and
                    self._board[line[2]] == self._board[line[1]] and
                        self._board[line[2]] != " "):
                    self._winner = self._board[line[2]]

    def __getitem__(self, key):
        return self._board[key]

    def __setitem__(self, key, value):
        if key not in self._board.keys():
            raise InvalidKey
        if self._board[key] != " ":
            raise InvalidMove
        if value not in ("X", "O"):
            raise InvalidValue
        if self._previous and value == self._previous:
            raise NotYourTurn

        self._previous = value
        self._board[key] = value
        self.update_winner()

    def game_status(self):
        self.update_winner()
        if self._winner:
            return str(self._winner + " wins!")
        if " " not in self._board.values():
            return "Draw!"
        return "Game in progress."

    def __str__(self):
        return '''
  -------------
3 | {A3} | {B3} | {C3} |
  -------------
2 | {A2} | {B2} | {C2} |
  -------------
1 | {A1} | {B1} | {C1} |
  -------------
    A   B   C  \n'''.format(**self._board)
