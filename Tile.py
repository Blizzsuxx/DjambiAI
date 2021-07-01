
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
            Game.SELECTED_PIECE_MOVES = moves
            for move in moves:
                if move.tile.piece is not None:
                    Game.TILES[move.tile.x][move.tile.y].setColor("purple")
                else:
                    Game.TILES[move.tile.x][move.tile.y].setColor("orange")
        else:
            Game.SELECTED_PIECE_MOVES = None
        print(self.x, self.y)
        return
    


    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            if Game.SELECTED_PIECE_MOVES is None:
                self.clicked_event()
            else:
                self.doMove()
                Game.SELECTED_PIECE_MOVES = None
                Game.draw()
        elif QMouseEvent.button() == QtCore.Qt.RightButton:
            #do what you want here
            Game.SELECTED_PIECE_MOVES = None
            print("Right Button Clicked")
            Game.draw()




    def doMove(self):
        bodyPlacementMoves = None
        for move in Game.SELECTED_PIECE_MOVES:
            if move.tile is self:
                bodyPlacementMoves = move.piece.doMove(move)
                self.piece = move.piece
                move.tileFrom.piece = None
        return bodyPlacementMoves