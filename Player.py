
from Piece import Piece


class Player:

    __slots__ = 'pieces'

    def __init__(self, color) -> None:
        self.pieces = (None)*9
        self.pieces[0] = Piece(color, Piece.TYPE.Chief, 0, 0) #1

        self.pieces[1] = Piece(color, Piece.TYPE.Assassin, 1, 0) #2

        self.pieces[2] = Piece(color, Piece.TYPE.Reporter, 0, 1) #3
        
        self.pieces[3] = Piece(color, Piece.TYPE.Diplomat, 1, 1) #4

        self.pieces[4] = Piece(color, Piece.TYPE.Necromobile, 2, 2) #5

        self.pieces[5] = Piece(color, Piece.TYPE.Militants, 2, 0) #6
        self.pieces[6] = Piece(color, Piece.TYPE.Militants, 2, 1) #7
        self.pieces[7] = Piece(color, Piece.TYPE.Militants, 0, 2) #8
        self.pieces[8] = Piece(color, Piece.TYPE.Militants, 1, 2) #9
