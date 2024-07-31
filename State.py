class State(object):
    """State

    Parameter
    ---------
    kinds: int, default=3
        Number of types of pieces.
        Defaults are large, medium, and small.
    """
    def __init__(self, kinds=3) -> None:
        self._list = [0 for i in range(9)]
        self._player_piece = {3**i:2 for i in range(kinds)}
        self._cpu_piece = {3**i:2 for i in range(kinds)}
        self._kinds = kinds

    def get_board_list(self):
        return self._list

    def set_board_list(self, board):
        self._list = board

    def get_player_piece(self):
        return self._player_piece

    def set_player_piece(self, piece):
        self._player_piece = piece

    def get_cpu_piece(self):
        return self._cpu_piece

    def set_cpu_piece(self, piece):
        self._cpu_piece = piece

    def get_kinds(self):
        return self._kinds

    def get_piece(self, turn):
        if turn == -1:
            return self._player_piece
        elif turn == 1:
            return self._cpu_piece

    def set_piece(self, turn, piece):
        if turn == -1:
            self._player_piece = piece
        elif turn == 1:
            self._cpu_piece = piece
