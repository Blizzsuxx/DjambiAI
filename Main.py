from Player import Player
from Piece import Piece
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QLabel

# Only needed for access to command line arguments
import sys

from Config import Config
    


def main():
    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = QWidget()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.


    grid = QGridLayout()
    grid.columnCount = Config.COLUMN_COUNT
    grid.rowCount = Config.ROW_COUNT

    Config.PLAYERS[0] = Player(Piece.COLOR.green)
    Config.PLAYERS[1] = Player(Piece.COLOR.yellow)
    Config.PLAYERS[2] = Player(Piece.COLOR.red)
    Config.PLAYERS[3] = Player(Piece.COLOR.blue)

    window.setLayout(grid)
    
    for i in range(Config.ROW_COUNT):
        for j in range(Config.COLUMN_COUNT):
            
            label = QLabel()
            label.setStyleSheet("QLabel { background-color : "+Config.COLOR_TILE[(j+i)%2]+"; }")
            label.size = (Config.TYLE_SIZE, Config.TYLE_SIZE)
            grid.addWidget(label, i, j)
            
    
    for player in Config.PLAYERS:
        for piece in player.pieces:
            button = QPushButton()
            button.setStyleSheet("QPushButton { background-color : " + piece.color.name + "; }")
            button.size = (Config.TYLE_SIZE, Config.TYLE_SIZE)
            grid.addWidget(button, piece.x, piece.y)
    app.exec()





if __name__ == '__main__':
    main()


