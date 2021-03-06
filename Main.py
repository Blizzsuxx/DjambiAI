from MinMaxTree import MinMaxTree
from Tile import CustomButton, Tile
from Player import Player
from Piece import Piece
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QSpinBox, QTextEdit, QWidget, QGridLayout, QLabel

# Only needed for access to command line arguments
import sys

from Game import Game
    


def main():



    Game.init()


    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = QWidget()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.


    grid = QGridLayout()
    grid.columnCount = Game.COLUMN_COUNT
    grid.rowCount = Game.ROW_COUNT

    Game.PLAYERS[0] = Player(Piece.COLOR.green)
    Game.PLAYERS[1] = Player(Piece.COLOR.yellow)
    Game.PLAYERS[2] = Player(Piece.COLOR.red)
    Game.PLAYERS[3] = Player(Piece.COLOR.blue)

    window.setLayout(grid)
    grid.setSpacing(0)
    grid.setContentsMargins(0,0,0,0)
    for i in range(Game.COLUMN_COUNT):
        for j in range(Game.ROW_COUNT):
            tile = Tile(i, j)
            button = CustomButton(tile)
            Game.TILES_VIEW[i][j] = button
            Game.TILES[i][j] = tile
            button.setColor(Game.COLOR_TILE[(j+i)%2])
            button.size = (Game.TYLE_SIZE, Game.TYLE_SIZE)
            button.setMinimumSize(QtCore.QSize(Game.TYLE_SIZE, Game.TYLE_SIZE))
            button.clicked.connect(button.clicked_event)
            grid.addWidget(button, j, i)
    
    Game.CENTER_TILE_VIEW = Game.TILES_VIEW[Game.COLUMN_COUNT // 2][Game.ROW_COUNT // 2]
    Game.CENTER_TILE = Game.TILES[Game.COLUMN_COUNT // 2][Game.ROW_COUNT // 2]
            
    for player in Game.PLAYERS:
        for piece in player.pieces:
            button = Game.TILES_VIEW[piece.x][piece.y]
            
            button.setColor(piece.color.name)
            button.setText(piece.__class__.__name__ )
            button.tile.piece = piece
    
    m = MinMaxTree()
    #m.getMove()
    doAction = QPushButton()
    doAction.setText("Do")
    undoAction = QPushButton()
    undoAction.setText("Undo")
    skipAction = QPushButton()
    skipAction.setText("Skip")
    skipAction.setMinimumSize(QtCore.QSize(Game.TYLE_SIZE, Game.TYLE_SIZE))
    doAction.setMinimumSize(QtCore.QSize(Game.TYLE_SIZE, Game.TYLE_SIZE))
    undoAction.setMinimumSize(QtCore.QSize(Game.TYLE_SIZE, Game.TYLE_SIZE))
    
    Game.MINMAX = m


    doAction.clicked.connect(CustomButton.doBestMove)
    undoAction.clicked.connect(CustomButton.undoMove)
    skipAction.clicked.connect(CustomButton.skip)

    grid.addWidget(doAction)
    grid.addWidget(undoAction)
    grid.addWidget(skipAction)

    currentPlayerLabel = QLabel()
    grid.addWidget(currentPlayerLabel)
    Game.CURRENT_PLAYER_LABEL = currentPlayerLabel


    Game.CURRENT_PLAYER_LABEL.setText(Game.PLAYERS[Game.CURRENT_PLAYER].color.name)


    Game.draw()
    window.move(500,50)
    app.exec()





if __name__ == '__main__':
    main()


