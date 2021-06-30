
from Game import Game
from PyQt5 import QtCore
from PyQt5 import QtWidgets
class Tile(QtWidgets.QPushButton):

    __slots__ = 'piece'
    def __init__(self) -> None:
        super().__init__()
        self.piece = None
    
    
    def setColor(self, color):

        self.setStyleSheet("QPushButton { background-color : " + color + "; }")


        return
    
    def clicked(self, checked: bool) -> None:

        Game.draw()

        if self.piece is not None:
            moves = self.piece.moves()
            for move in moves:
                Game.TILES[move.x][move.y].setColor("red")
        


        return super().clicked(checked=checked)

    