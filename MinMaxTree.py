
from Game import Game
from Node import Node


class MinMaxTree:

    __slots__ = 'root'

    def __init__(self) -> None:
        self.root = Node(Game.TILES.copy(), Game.PLAYERS[0])