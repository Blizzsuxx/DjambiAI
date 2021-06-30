from enum import Enum


class Piece:



    COLOR = Enum('COLOR', 'green yellow red blue')
    TYPE = Enum('TYPE', 'Chief Assassin Reporter Militants Diplomat Necromobile')



    __slots__ = 'color', 'type', 'x', 'y'

    def __init__(self, color, x, y) -> None:
        self.color = color
        self.x = x
        self.y = y



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
