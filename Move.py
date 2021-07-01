
class Move:

    __slots__ = 'piece', 'tile', 'tileFrom'


    DIRECTIONS = (
                    (-1, -1), (0, -1), (1, -1),
                    (-1, 0), (1, 0),        #skipping (0, 0)
                    (-1, 1), (0, 1), (1, 1)
                    )

    def __init__(self, piece, tile, tileFrom) -> None:
        self.piece = piece
        self.tile = tile
        self.tileFrom = tileFrom