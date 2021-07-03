
import Piece


class Move:

    __slots__ = 'piece', 'tile', 'tileFrom', 'bodyMoves'


    DIRECTIONS = (
                    (-1, -1), (0, -1), (1, -1),
                    (-1, 0), (1, 0),        #skipping (0, 0)
                    (-1, 1), (0, 1), (1, 1)
                    )

    def __init__(self, piece, tile, tileFrom) -> None:
        self.piece = piece
        self.tile = tile
        self.tileFrom = tileFrom
        self.bodyMoves = None
    
    def execute(self):
        self.piece.takeMoveCoordinates(self)
        if self.tile.piece is not None:
            self.tile.piece.dead = True
        self.tile.piece = self.piece
        self.tileFrom.piece = None

        if self.bodyMoves:
            self.bodyMoves.piece.takeMoveCoordinates(self.bodyMoves)
            self.bodyMoves.tile.piece = self.bodyMoves.piece
            if not isinstance(self.piece, Piece.Reporter): 
                self.bodyMoves.tileFrom.piece = self.piece
    

    def undo(self):
        if self.bodyMoves:
            self.bodyMoves.piece.undoMoveCoordinates(self.bodyMoves)
            self.bodyMoves.tileFrom.piece = self.bodyMoves.piece
            if not isinstance(self.piece, Piece.Reporter): 
                self.bodyMoves.tile.piece = None
        self.piece.undoMoveCoordinates(self)
        if self.tile.piece is not None and not isinstance(self.piece, Piece.Necromobile):
            self.tile.piece.dead = False
        self.tileFrom.piece = self.piece
        if self.tile.piece is self.tileFrom.piece:
            self.tile.piece = None

