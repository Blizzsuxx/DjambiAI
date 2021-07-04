
from Game import Game


class Node:

    __slots__ = 'move', 'children', 'player', 'values', 'playerId', 'chosen'

    def __init__(self, move, playerId) -> None:
        self.move = move
        self.children = []
        self.playerId = playerId
        self.player = Game.PLAYERS[playerId]
        self.values = [0,0,0,0]
        self.chosen = None
    