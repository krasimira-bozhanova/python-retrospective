WINNING_COMBINATIONS = (["A1", 'A2', "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"],
                ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"],
                ["A1", "B2", "C3"], ["A3", "B2", "C1"])


class InvalidMove(Exception):
    pass


class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:

    def __init__(self):
            self.board = {'A1': " ", 'A2': " ", 'A3': " ",
                          'B1': " ", 'B2': " ", 'B3': " ",
                          'C1': " ", 'C2': " ", 'C3': " "}
            self.played = False
            self.winner = ""

    def __getitem__(self, key):
        return self.board[key]

    def __setitem__(self, key, value):
        if key not in self.board.keys():
            raise InvalidKey
        if self.board[key] != " ":
            raise InvalidMove
        if value not in ("X", "O"):
            raise InvalidValue
        if self.played and value == self.turn:
            raise NotYourTurn

        if not self.played:
            self.played = True

        self.turn = value
        self.board[key] = value
        self.game_status()

    def game_status(self):
        if self.winner == "":
            for triple in WINNING_COMBINATIONS:
                if (self.board[triple[0]] == self.board[triple[1]] and
                    self.board[triple[2]] == self.board[triple[1]] and
                        self.board[triple[2]] != " "):
                    self.winner = self.board[triple[2]]

        if self.winner != "":
            return str(self.winner + " wins!")

        if " " not in self.board.values():
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
    A   B   C  \n'''.format(**self.board)
