class State(object):
    """State

    Parameter
    ---------
    kinds: int, default=3
        Number of types of pieces.
        Defaults are large, medium, and small.

    win: int, default=0
        player win -> -1
        cpu win    -> 1
        None win   -> 0

    reach: int, default=0
        player reach -> -1
        cpu reach    -> 1
        None reach   -> 0
    """
    def __init__(self, kinds=3, win=0, reach=0) -> None:
        self._list = [0 for i in range(9)]
        self._player_piece = {3**i:2 for i in range(kinds)}
        self._cpu_piece = {3**i:2 for i in range(kinds)}
        self._kinds = kinds
        self._win = win
        self._reach = reach

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

    def get_win(self):
        return self._win

    def set_win(self, win):
        self._win = win

    def get_reach(self):
        return self._reach

    def set_reach(self, reach):
        self._reach = reach
