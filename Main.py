from Piece import Piece
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel

# Only needed for access to command line arguments
import sys

ROW_COUNT = 9
COLUMN_COUNT = 9
COLOR_TILE = ["black", "white"]



def generatePieces(x,y):
    if x == 0 and y == 0:

        piece = Piece(Piece.COLOR.green, Piece.TYPE.Chief, x, y)
    


def main():
    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = QWidget()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.


    grid = QGridLayout()
    grid.columnCount = COLUMN_COUNT
    grid.rowCount = ROW_COUNT

    

    window.setLayout(grid)
    
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            
            label = QLabel()
            label.setStyleSheet("QLabel { background-color : "+COLOR_TILE[(j+i)%2]+"; }")
            label.size = (100, 100)
            grid.addWidget(label, i, j)
    
        
    app.exec()





if __name__ == '__main__':
    main()


