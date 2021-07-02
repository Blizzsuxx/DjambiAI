from Move import Move
from Game import Game
from enum import Enum


class Piece:



    COLOR = Enum('COLOR', 'green yellow red blue')
    TYPE = Enum('TYPE', 'Chief Assassin Reporter Militants Diplomat Necromobile')



    __slots__ = 'color', 'x', 'y', 'dead'

    def __init__(self, color, x, y) -> None:
        self.color = color
        self.x = x
        self.y = y
        self.dead = False
    

    def raycast(self, directionX, directionY):
        movesList = []
        currentPointX = self.x
        currentPointY = self.y
        currentPointX += directionX
        currentPointY += directionY
        while currentPointX >= 0 and currentPointX < Game.COLUMN_COUNT and currentPointY >= 0 and currentPointY < Game.ROW_COUNT:
            destination = Game.TILES[currentPointX][currentPointY]
            if destination.piece is not None:
                #if destination.piece.color != tile.piece.color:
                self.captureEvent(movesList, destination)
                return movesList
            
            
            currentPointX += directionX
            currentPointY += directionY
            if destination.isCenter():
                continue

            newMove = Move(self, destination, Game.TILES[self.x][self.y])
            movesList.append(newMove)
        return movesList
    
    def moves(self):
        movesList = []
        for direction in Move.DIRECTIONS:
            movesList.extend(self.raycast(direction[0], direction[1]))

        return movesList
    

    # this gets overriden by other pieces
    def captureEvent(self, movesList, destination):
        if not destination.piece.dead:
            newMove = Move(self, destination, Game.TILES[self.x][self.y])
            movesList.append(newMove)


    def doMove(self, move):
        self.x = move.tile.x
        self.y = move.tile.y
        bodyMoves = None
        if move.tile.piece is not None:
            move.tile.piece.dead = True
            bodyMoves = []
            for column in Game.TILES:
                for destination in column:
                    if destination.piece is not None and destination.piece is not self or destination.isCenter():
                        continue

                    newMove = Move(move.tile.piece, destination, Game.TILES[move.tile.x][move.tile.y])
                    bodyMoves.append(newMove)

        return bodyMoves












class Chief(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
    


    def raycast(self, directionX, directionY):
        movesList = []
        currentPointX = self.x
        currentPointY = self.y
        currentPointX += directionX
        currentPointY += directionY
        while currentPointX >= 0 and currentPointX < Game.COLUMN_COUNT and currentPointY >= 0 and currentPointY < Game.ROW_COUNT:
            destination = Game.TILES[currentPointX][currentPointY]
            if destination.piece is not None:
                #if destination.piece.color != tile.piece.color:
                self.captureEvent(movesList, destination)
                return movesList
            
            
            currentPointX += directionX
            currentPointY += directionY

            newMove = Move(self, destination, Game.TILES[self.x][self.y])
            movesList.append(newMove)
        return movesList




class Assassin(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
    


    #assasin puts the body where he came from
    def doMove(self, move):
        self.x = move.tile.x
        self.y = move.tile.y
        bodyMoves = None
        if move.tile.piece is not None:
            move.tile.piece.dead = True
            bodyMoves = []
            newMove = Move(move.tile.piece,Game.TILES[move.tileFrom.x][move.tileFrom.y], Game.TILES[move.tile.x][move.tile.y])
            bodyMoves.append(newMove)
            

        return bodyMoves


class Reporter(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
    
    #reporter cannot capture pieces by going over them
    def captureEvent(self, movesList, destination):
        return 
    

    def doMove(self, move):
        self.x = move.tile.x
        self.y = move.tile.y
        bodyMoves = []
        tile = Game.TILES[move.tile.x-1][move.tile.y]
        if tile.piece is not None and not tile.piece.dead and tile.piece is not self:
            newMove = Move(tile.piece, tile, tile)
            bodyMoves.append(newMove)
        tile = Game.TILES[move.tile.x+1][move.tile.y]
        if tile.piece is not None and not tile.piece.dead and tile.piece is not self:
            newMove = Move(tile.piece, tile, tile)
            
            bodyMoves.append(newMove)
        tile = Game.TILES[move.tile.x][move.tile.y-1]
        if tile.piece is not None and not tile.piece.dead and tile.piece is not self:
            newMove = Move(tile.piece, tile, tile)
            
            bodyMoves.append(newMove)
        tile = Game.TILES[move.tile.x][move.tile.y+1]
        if tile.piece is not None and not tile.piece.dead and tile.piece is not self:
            newMove = Move(tile.piece, tile, tile)
            
            bodyMoves.append(newMove)
        print(bodyMoves)
        if len(bodyMoves) == 0:
            bodyMoves = None
        return bodyMoves


class Militants(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
    
    def raycast(self, directionX, directionY):
        movesList = []
        currentPointX = self.x
        currentPointY = self.y
        currentPointX += directionX
        currentPointY += directionY
        maximumNumberOfSteps = 2 #militants can only move for 2 squares
        currentStep = 0
        while currentPointX >= 0 and currentPointX < Game.COLUMN_COUNT and currentPointY >= 0 and currentPointY < Game.ROW_COUNT and currentStep < maximumNumberOfSteps:
            destination = Game.TILES[currentPointX][currentPointY]
            currentStep+=1
            if destination.piece is not None:
                #if destination.piece.color != tile.piece.color:
                self.captureEvent(movesList, destination)
                return movesList

            
            currentPointX += directionX
            currentPointY += directionY
            if destination.isCenter():
                continue

            newMove = Move(self, destination, Game.TILES[self.x][self.y])
            movesList.append(newMove)
        return movesList
    

    def captureEvent(self, movesList, destination):
        if destination.isCenter():
            return
        return super().captureEvent(movesList, destination)


class Diplomat(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
    
    def captureEvent(self, movesList, destination):
        #Diplomat cannot attack, that is move, friendly pieces or dead pieces
        if destination.piece.color != self.color and not destination.piece.dead:
            newMove = Move(self, destination, Game.TILES[self.x][self.y])
            movesList.append(newMove)
        

    def doMove(self, move):
        #Diplomat does not kill pieces
        self.x = move.tile.x
        self.y = move.tile.y
        bodyMoves = None
        if move.tile.piece is not None:
            bodyMoves = []
            for column in Game.TILES:
                for destination in column:
                    if destination.piece is not None and destination.piece is not self or destination.isCenter():
                        continue

                    newMove = Move(move.tile.piece, destination, Game.TILES[move.tile.x][move.tile.y])
                    bodyMoves.append(newMove)

        return bodyMoves


class Necromobile(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
    
    def captureEvent(self, movesList, destination):
        
        #Necromobile can only attack dead pieces
        if destination.piece.dead:
            newMove = Move(self, destination, Game.TILES[self.x][self.y])
            movesList.append(newMove)
