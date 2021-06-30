
from Piece import Piece, Assassin, Chief, Diplomat, Militants, Necromobile, Reporter
from Game import Game

class Player:

    __slots__ = 'pieces'

    def __init__(self, color) -> None:
        self.pieces = [None]*9

        x,y = 0,0
        i,j = 1,1

        if color == Piece.COLOR.green:
            pass
        elif color == Piece.COLOR.yellow:
            x,y = Game.COLUMN_COUNT-1,0
            i,j = -1,1
        elif color == Piece.COLOR.red:
            x,y = 0,Game.ROW_COUNT-1
            i,j = 1,-1
        elif color == Piece.COLOR.blue:
            x,y = Game.COLUMN_COUNT-1,Game.ROW_COUNT-1
            i,j = -1,-1


        self.pieces[0] = Chief(color, x, y) #1

        self.pieces[1] = Assassin(color, x+i, y) #2

        self.pieces[2] = Reporter(color, x, y+j) #3
        
        self.pieces[3] = Diplomat(color, x+i, y+j) #4

        self.pieces[4] = Necromobile(color, x+i+i, y+j+j) #5

        self.pieces[5] = Militants(color, x+i+i, y) #6
        self.pieces[6] = Militants(color, x+i+i, y+j) #7
        self.pieces[7] = Militants(color, x, y+j+j) #8
        self.pieces[8] = Militants(color, x+i, y+j+j) #9
