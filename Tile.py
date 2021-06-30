
from Game import Game
from PyQt5 import QtCore
from PyQt5 import QtWidgets
class Tile(QtWidgets.QPushButton):

    __slots__ = 'piece', 'x', 'y'
    def __init__(self, x, y) -> None:
        super().__init__()
        self.piece = None
        self.x = x
        self.y = y
    
    
    def setColor(self, color):

        self.setStyleSheet("QPushButton { background-color : " + color + "; }")


        return
    
    def clicked_event(self) -> None:

        Game.draw()
        if self.piece is not None:
            moves = self.piece.moves()
            for move in moves:
                Game.TILES[move.tile.x][move.tile.y].setColor("orange")
        print(self.x, self.y)
        return


    