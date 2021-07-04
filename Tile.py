
from Node import Node
from Piece import Diplomat, Reporter
from Game import Game
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import time

class CustomButton(QtWidgets.QPushButton):

    __slots__ = 'tile'
    def __init__(self, tile) -> None:
        super().__init__()
        self.tile = tile
    

    def setColor(self, color):

        self.setStyleSheet("QPushButton { background-color : " + color + "; }")


        return
    
    def clicked_event(self) -> None:

        Game.draw()
        if self.tile.piece is not None and not self.tile.piece.dead:
            Game.CURRENT_STATE = Game.STATES.move
            moves = self.tile.piece.moves()
            Game.SELECTED_PIECE_MOVES = moves
            for move in moves:
                if move.tile.piece is not None:
                    Game.TILES_VIEW[move.tile.x][move.tile.y].setColor("purple")
                else:
                    Game.TILES_VIEW[move.tile.x][move.tile.y].setColor("orange")
        else:
            Game.SELECTED_PIECE_MOVES = None
            Game.CURRENT_STATE = Game.STATES.select
        print(self.tile.x, self.tile.y)
        return
    
    @staticmethod
    def skip():
        Game.getNextPlayer()
        Game.MINMAX.root = Node(None, Game.CURRENT_PLAYER)
        Game.CURRENT_PLAYER_LABEL.setText(Game.PLAYERS[Game.CURRENT_PLAYER].color.name)

        Game.draw()

    @staticmethod
    def undoMove():
        Game.getPreviousPlayer()
        Game.LAST_MOVE.pop().undo()
        Game.MINMAX.root = Node(None, Game.CURRENT_PLAYER)
        Game.CURRENT_PLAYER_LABEL.setText(Game.PLAYERS[Game.CURRENT_PLAYER].color.name)
        Game.draw()
        
    @staticmethod
    def doBestMove():
        #do what you want here
            if Game.CURRENT_STATE == Game.STATES.place:
                return
            Game.SELECTED_PIECE_MOVES = None
            Game.CURRENT_STATE = Game.STATES.select

            Game.MOVE_START_TIME = time.time()
            bestValue, bestNode = Game.MINMAX.getMove()
            bestNode.chosen.move.execute()
            
            Game.LAST_MOVE.append(bestNode.chosen.move)
            Game.getNextPlayer()
            Game.MINMAX.root = Node(None, Game.CURRENT_PLAYER)
            Game.CURRENT_PLAYER_LABEL.setText(Game.PLAYERS[Game.CURRENT_PLAYER].color.name)

            Game.draw()

            Game.TILES_VIEW[bestNode.chosen.move.tileFrom.x][bestNode.chosen.move.tileFrom.y].setColor("orange")
            Game.TILES_VIEW[bestNode.chosen.move.tile.x][bestNode.chosen.move.tile.y].setColor("purple")
            if bestNode.chosen.move.bodyMoves:
                Game.TILES_VIEW[bestNode.chosen.move.bodyMoves.tileFrom.x][bestNode.chosen.move.bodyMoves.tileFrom.y].setColor("orange")
                Game.TILES_VIEW[bestNode.chosen.move.bodyMoves.tile.x][bestNode.chosen.move.bodyMoves.tile.y].setColor("purple")


    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            if Game.CURRENT_STATE == Game.STATES.select:
                self.clicked_event()
            elif Game.CURRENT_STATE == Game.STATES.move:
                
                bodyMoves = self.tile.doMove()
                Game.draw()
                Game.CURRENT_STATE = Game.STATES.select
                if bodyMoves is not None:
                    Game.CURRENT_STATE = Game.STATES.place
                    for move in bodyMoves:
                        if move.tile.piece is not None:
                            Game.TILES_VIEW[move.tile.x][move.tile.y].setColor("purple")
                        else:
                            Game.TILES_VIEW[move.tile.x][move.tile.y].setColor("orange")
                Game.SELECTED_PIECE_MOVES = bodyMoves
            elif Game.CURRENT_STATE == Game.STATES.place:
                playerPickedAvailableTile = self.tile.doMoveBody()
                if playerPickedAvailableTile or isinstance(Game.PREVIOUS_MOVE.piece, Reporter):
                    Game.CURRENT_STATE = Game.STATES.select
                    Game.draw()
        elif QMouseEvent.button() == QtCore.Qt.RightButton:
            self.doBestMove()




class Tile():

    __slots__ = 'piece', 'x', 'y'
    def __init__(self, x, y) -> None:
        super().__init__()
        self.piece = None
        self.x = x
        self.y = y




    def doMove(self):
        bodyPlacementMoves = None
        for move in Game.SELECTED_PIECE_MOVES:
            if move.tile is self:
                bodyPlacementMoves = move.piece.doMove(move)
                self.piece = move.piece
                move.tileFrom.piece = None

                Game.PREVIOUS_MOVE = move
        return bodyPlacementMoves
    
    def doMoveBody(self):
        for move in Game.SELECTED_PIECE_MOVES:
            if move.tile is self:
                
                move.piece.doMove(move)
                self.piece = move.piece
                if not isinstance(Game.PREVIOUS_MOVE.piece, Reporter): 
                    move.tileFrom.piece = Game.PREVIOUS_MOVE.piece
                return True
        return False
    


    def isCenter(self):
        if self is Game.CENTER_TILE:
            return True
        return False