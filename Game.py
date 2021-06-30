
class Game:

    ROW_COUNT = 9
    COLUMN_COUNT = 9
    COLOR_TILE = ["black", "white"]
    TYLE_SIZE = 100
    PLAYERS = [None]*4

    TILES = None

    @staticmethod
    def init():
        Game.TILES = [[None]*Game.COLUMN_COUNT for i in range(Game.ROW_COUNT)]

    @staticmethod
    def draw():



        for i in range(Game.COLUMN_COUNT):
            for j in range(Game.ROW_COUNT):
                button = Game.TILES[i][j]
                button.setColor(Game.COLOR_TILE[(j+i)%2])

                button.setText("")
        
                
        for player in Game.PLAYERS:
            for piece in player.pieces:
                button = Game.TILES[piece.x][piece.y]
                
                button.setColor(piece.color.name)
                
                button.setText(piece.__class__.__name__ )