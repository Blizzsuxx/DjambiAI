
class Node:

    __slots__ = 'move', 'children', 'player', 'values'

    def __init__(self, boardState, player) -> None:
        self.move = boardState
        self.children = []
        self.player = player
        self.values = [0,0,0,0]