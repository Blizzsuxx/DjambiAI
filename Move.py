
class Move:

    __slots__ = 'piece', 'tile'


    DIRECTIONS = (
                    (-1, -1), (0, -1), (1, -1),
                    (-1, 0), (0, 0), (1, 0),
                    (-1, 1), (0, 1), (1, 1)
                    )

    def __init__(self, piece, tile) -> None:
        self.piece = piece
        self.tile = tile