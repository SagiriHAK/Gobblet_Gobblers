class Operator(object):
    """Operator

    Parameter
    ---------
    turn: {-1, 1}
        Player or CPU

    source: int
        If a piece is moved, the number of the board on which the piece is placed.
        To move a piece from the hand; -1.

    dist: int
        The number of the destination board on which the pieces are to be moved.

    size: int
        Piece size; 1, 3, 9
        Follow the table below.

    Piece size
    ============
    small      1
    middle     3
    large      9
    ============
    """
    def __init__(self, turn, source, dist, size) -> None:
        self._turn = turn
        self._source = source
        self._dist = dist
        self._size = size

    def get_all_param(self):
        return self._turn, self._source, self._dist, self._size

    def get_turn(self):
        return self._turn

    def get_source(self):
        return self._source

    def get_dist(self):
        return self._dist

    def get_size(self):
        return self._size
