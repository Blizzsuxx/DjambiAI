from Move import Move
from Game import Game
from enum import Enum


class Piece:



    COLOR = Enum('COLOR', 'green yellow red blue')
    TYPE = Enum('TYPE', 'Chief Assassin Reporter Militants Diplomat Necromobile')



    __slots__ = 'color', 'type', 'x', 'y'

    def __init__(self, color, x, y) -> None:
        self.color = color
        self.x = x
        self.y = y
    
    @staticmethod
    def raycast(tile, directionX, directionY):
        movesList = []
        currentPointX = tile.x
        currentPointY = tile.y
        currentPointX += directionX
        currentPointY += directionY
        while currentPointX >= 0 and currentPointX < Game.COLUMN_COUNT and currentPointY >= 0 and currentPointY < Game.ROW_COUNT:
            destination = Game.TILES[currentPointX][currentPointY]

            if destination.piece is not None:
                if destination.piece.color != tile.piece.color:
                    newMove = Move(tile.piece, destination)
                    movesList.append(newMove)
                return movesList

            newMove = Move(tile.piece, destination)
            movesList.append(newMove)
            currentPointX += directionX
            currentPointY += directionY
        return movesList
    
    def moves(self):
        movesList = []
        for direction in Move.DIRECTIONS:
            movesList.extend(Piece.raycast(Game.TILES[self.x][self.y], direction[0], direction[1]))

        return movesList
    





class Chief(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)


class Assassin(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)


class Reporter(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)


class Militants(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)


class Diplomat(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)


class Necromobile(Piece):

    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
