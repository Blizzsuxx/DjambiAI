from enum import Enum


class Piece:



    COLOR = Enum('COLOR', 'green yellow red blue')
    TYPE = Enum('TYPE', 'Chief Assassin Reporter Militants Diplomat Necromobile')



    __slots__ = 'color', 'type', 'x', 'y'

    def __init__(self, color, type, x, y) -> None:
        self.color = color
        self.type = type
        self.x = x
        self.y = y