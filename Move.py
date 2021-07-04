
from Game import Game
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
        
        if self.tile.piece is not None and not isinstance(self.piece, Piece.Diplomat):
            self.tile.piece.dead = True
            if isinstance(self.tile.piece, Piece.Chief):
                ownerOfDead = Game.getPlayerOfColor(self.tile.piece.color)
                ownerOfKiller = Game.getPlayerOfColor(self.piece.color)
                newPieces = []
                for piece in ownerOfDead.pieces:
                    if not piece.dead and not isinstance(piece, Piece.Chief):
                        ownerOfKiller.pieces.append(piece)
                        piece.originalColor.append(ownerOfDead.color)
                        piece.color = ownerOfKiller.color
                    else:
                        newPieces.append(piece)
                ownerOfDead.pieces = newPieces
                #print("do", ownerOfDead.pieces, ownerOfKiller.pieces)
                
        self.tile.piece = self.piece
        self.tileFrom.piece = None
        print("DO")
        print(self.piece.__class__.__name__, self.tileFrom.x, self.tileFrom.y, self.tile.x, self.tile.y)


        if self.bodyMoves:
            self.bodyMoves.piece.takeMoveCoordinates(self.bodyMoves)
            self.bodyMoves.tile.piece = self.bodyMoves.piece
            print(self.bodyMoves.tile.x, self.bodyMoves.tile.y)

            if not isinstance(self.piece, Piece.Reporter): 
                self.bodyMoves.tileFrom.piece = self.piece
            else:
                self.bodyMoves.tile.piece.dead = True
    

    def undo(self):
        
        if self.bodyMoves:
            self.bodyMoves.piece.undoMoveCoordinates(self.bodyMoves)
            #print(self.bodyMoves.tile.x, self.bodyMoves.tile.y)

            self.bodyMoves.tileFrom.piece = self.bodyMoves.piece
            if not isinstance(self.piece, Piece.Reporter): 
                self.bodyMoves.tile.piece = None
            else:
                self.bodyMoves.tile.piece.dead = False
        self.piece.undoMoveCoordinates(self)



        if self.tile.piece is not None and not isinstance(self.piece, Piece.Necromobile) and self.tile.piece.dead:
            self.tile.piece.dead = False


            if isinstance(self.tile.piece, Piece.Chief):
                ownerOfDead = Game.getPlayerOfColor(self.tile.piece.color)
                ownerOfKiller = Game.getPlayerOfColor(self.piece.color)
                newPieces = []
                for piece in ownerOfKiller.pieces:
                    if piece.originalColor[-1] == ownerOfDead.color:
                        ownerOfDead.pieces.append(piece)
                        piece.originalColor.pop()
                        piece.color = ownerOfDead.color
                    else:
                        newPieces.append(piece)
                ownerOfKiller.pieces = newPieces
                #print("undo", ownerOfDead.pieces, ownerOfKiller.pieces)


            print("UNDO")
            print(self.piece.__class__.__name__, self.tileFrom.x, self.tileFrom.y, self.tile.x, self.tile.y)
            #if self.bodyMoves:
                #print(self.bodyMoves.piece.__class__.__name__, self.bodyMoves.tileFrom.x, self.bodyMoves.tileFrom.y, self.bodyMoves.tile.x, self.bodyMoves.tile.y)
        self.tileFrom.piece = self.piece
        if self.tile.piece is self.tileFrom.piece:
            self.tile.piece = None

