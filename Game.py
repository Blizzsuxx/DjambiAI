
from enum import Enum
import copy
class Game:

    ROW_COUNT = 9
    COLUMN_COUNT = 9
    COLOR_TILE = ["black", "white"]
    TYLE_SIZE = 100
    DEPTH = 3
    STATES = Enum('STATES', 'select move place')

    HEURISTICS_UPPER_BOUND = 504
    MINMAX = None
    CURRENT_PLAYER = 0
    CURRENT_PLAYER_LABEL = None
    MOVE_START_TIME = None
    WAIT_TIME = 7
    DROP_RATE = 0
    LAST_MOVE = []
    CURRENT_PLAYER_BACKUP = None

    CURRENT_STATE = STATES.select


    PLAYERS = [None]*4
    PREVIOUS_MOVE = None

    TILES = None
    TILES_VIEW = None




    SELECTED_PIECE_MOVES = None
    CENTER_TILE = None
    CENTER_TILE_VIEW = None

    @staticmethod
    def init():
        Game.TILES = [[None]*Game.COLUMN_COUNT for i in range(Game.ROW_COUNT)]
        Game.TILES_VIEW = [[None]*Game.COLUMN_COUNT for i in range(Game.ROW_COUNT)]


    @staticmethod
    def draw():

        for i in range(Game.COLUMN_COUNT):
            for j in range(Game.ROW_COUNT):
                button = Game.TILES_VIEW[i][j]
                button.setColor(Game.COLOR_TILE[(j+i)%2])

                button.setText("")
        
        Game.CENTER_TILE_VIEW.setColor("grey")        
        for player in Game.PLAYERS:
            for piece in player.pieces:
                button = Game.TILES_VIEW[piece.x][piece.y]
                
                button.setColor(piece.color.name)
                
                if piece.dead:
                    button.setText(piece.__class__.__name__ + " \r\nDEAD")
                else:
                    button.setText(piece.__class__.__name__ )
        
    @staticmethod
    def copyTiles(tiles):
        return copy.deepcopy(tiles)
    

    @staticmethod
    def getPlayerOfColor(color):
        for player in Game.PLAYERS:
            if player.color == color:
                return player
    
    @staticmethod
    def getPlayerOfColorId(color):
        for i in range(len(Game.PLAYERS)):
            player = Game.PLAYERS[i]
            if player.color == color:
                return i
    
    
    @staticmethod
    def getNextPlayer():
        lord = Game.getLordPlayerId()
        if lord is not None:
            print("AA")
            if Game.CURRENT_PLAYER_BACKUP is None:
                Game.CURRENT_PLAYER_BACKUP = Game.CURRENT_PLAYER
                Game.CURRENT_PLAYER = lord
            else:
                Game.CURRENT_PLAYER = Game.CURRENT_PLAYER_BACKUP
                Game.CURRENT_PLAYER = (Game.CURRENT_PLAYER + 1) % len(Game.PLAYERS)
                if Game.CURRENT_PLAYER == lord:
                    Game.CURRENT_PLAYER = (Game.CURRENT_PLAYER + 1) % len(Game.PLAYERS)
                Game.CURRENT_PLAYER_BACKUP = None
        else:
            Game.CURRENT_PLAYER = (Game.CURRENT_PLAYER + 1) % len(Game.PLAYERS)
            Game.CURRENT_PLAYER_BACKUP = None
        while Game.PLAYERS[Game.CURRENT_PLAYER].isChiefDead():
            Game.CURRENT_PLAYER = (Game.CURRENT_PLAYER + 1) % len(Game.PLAYERS)
        return Game.CURRENT_PLAYER
    
    @staticmethod
    def getPreviousPlayer():
        lord = Game.getLordPlayerId()
        if lord is not None:
            if Game.CURRENT_PLAYER_BACKUP is None:
                Game.CURRENT_PLAYER_BACKUP = Game.CURRENT_PLAYER
                Game.CURRENT_PLAYER = lord
            else:
                Game.CURRENT_PLAYER = Game.CURRENT_PLAYER_BACKUP
                Game.CURRENT_PLAYER = (Game.CURRENT_PLAYER - 1) % len(Game.PLAYERS)
                Game.CURRENT_PLAYER_BACKUP = None
        else:
            Game.CURRENT_PLAYER = (Game.CURRENT_PLAYER - 1) % len(Game.PLAYERS)
        while Game.PLAYERS[Game.CURRENT_PLAYER].isChiefDead():
            Game.CURRENT_PLAYER = (Game.CURRENT_PLAYER - 1) % len(Game.PLAYERS)
        return Game.CURRENT_PLAYER
    
    @staticmethod
    def getLordPlayer():
        if Game.CENTER_TILE.piece:
            return Game.getPlayerOfColor(Game.CENTER_TILE.piece.color)
    

    @staticmethod
    def getLordPlayerId():
        if Game.CENTER_TILE.piece:
            return Game.getPlayerOfColorId(Game.CENTER_TILE.piece.color)