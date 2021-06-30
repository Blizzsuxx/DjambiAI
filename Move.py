
class Move:

    __slots__ = 'piece', 'tile'

    def __init__(self, piece, tile) -> None:
        self.piece = piece
        self.tile = tile