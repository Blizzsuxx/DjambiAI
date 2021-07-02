from enum import Enum

class Game:

    ROW_COUNT = 9
    COLUMN_COUNT = 9
    COLOR_TILE = ["black", "white"]
    TYLE_SIZE = 100
    DEPTH = 5
    PLAYERS = [None]*4
    PREVIOUS_MOVE = None

    TILES = None
    REAL_TILES = None


    STATES = Enum('STATES', 'select move place')

    CURRENT_STATE = STATES.select

    SELECTED_PIECE_MOVES = None
    CENTER_TILE = None
    

    @staticmethod
    def init():
        Game.TILES = [[None]*Game.COLUMN_COUNT for i in range(Game.ROW_COUNT)]
        Game.REAL_TILES = [[None]*Game.COLUMN_COUNT for i in range(Game.ROW_COUNT)]


    @staticmethod
    def draw():



        for i in range(Game.COLUMN_COUNT):
            for j in range(Game.ROW_COUNT):
                button = Game.TILES[i][j]
                button.setColor(Game.COLOR_TILE[(j+i)%2])

                button.setText("")
        
        Game.CENTER_TILE.setColor("grey")        
        for player in Game.PLAYERS:
            for piece in player.pieces:
                button = Game.TILES[piece.x][piece.y]
                
                button.setColor(piece.color.name)
                
                if piece.dead:
                    button.setText(piece.__class__.__name__ + " \r\nDEAD")
                else:
                    button.setText(piece.__class__.__name__ )
        
        