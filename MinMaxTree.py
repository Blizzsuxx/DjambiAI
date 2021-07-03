
from Game import Game
from Move import Move
from Node import Node
import Piece

class MinMaxTree:

    __slots__ = 'root'

    def __init__(self) -> None:
        self.root = Node(None, 0)
        
    

    def getMove(self, node=None, playerId=None, bound=Game.HEURISTICS_UPPER_BOUND, depth=0):
        if node is None:
            node = self.root
            playerId = self.root.playerId
        if node.move:
            node.move.execute()
        if depth == Game.DEPTH:
            self.heuristics(node)
            if node.move:
                node.move.undo()

            return (node.values, node)
        


        for piece in self.root.player.pieces:
            currentMoves = (piece.moves())
            
            for move in currentMoves:
                move.piece.bodyPlacementMoves(move)
                if move.bodyMoves:
                    for bodyMove in move.bodyMoves:
                        copyMove = Move(move.piece, move.tile, move.tileFrom)
                        copyMove.bodyMoves = bodyMove
                        self.root.children.append(Node(copyMove, 0))
                else:
                    self.root.children.append(Node(move, 0))
                break
            break
        best, bestNode = self.getMove(node.children[0], (playerId+1)%4, Game.HEURISTICS_UPPER_BOUND, depth+1)



        firstRun = True
        for i in range(0, len(self.root.player.pieces)):
            if firstRun:
                firstRun = False
                continue

            if best[playerId] >= bound:
                if node.move:
                    node.move.undo()
                return (best, bestNode)
            
            piece = self.root.player.pieces[i]
            currentMoves = (piece.moves())
            current = None
            for move in currentMoves:
                move.piece.bodyPlacementMoves(move)
                if move.bodyMoves:
                    for bodyMove in move.bodyMoves:
                        copyMove = Move(move.piece, move.tile, move.tileFrom)
                        copyMove.bodyMoves = bodyMove
                        newNode = Node(copyMove, 0)


                        self.root.children.append(newNode)
                        current, currentNode = self.getMove(newNode, (playerId+1)%4, Game.HEURISTICS_UPPER_BOUND - best[playerId])
                        if current[playerId] > best[playerId]:
                            best = current
                            bestNode = currentNode
                else:
                    newNode = Node(move, 0)
                    self.root.children.append(newNode)
                    current = self.getMove(newNode, (playerId+1)%4, Game.HEURISTICS_UPPER_BOUND - best[playerId])
                    if current[playerId] > best[playerId]:
                        best = current
                        bestNode = currentNode
        if node.move:
            node.move.undo()
        
        return (best, bestNode)
            
            
        
    


    def heuristics(self, node):
        for i in range(len(Game.PLAYERS)):
            player = Game.PLAYERS[i]
            for piece in player.pieces:
                if not piece.dead:
                    if isinstance(piece, Piece.Militants):
                        node.values[i] += 3
                    elif isinstance(piece, Piece.Diplomat):
                        node.values[i] += 6
                    elif isinstance(piece, Piece.Necromobile):
                        node.values[i] += 6
                    elif isinstance(piece, Piece.Assassin):
                        node.values[i] += 9
                    elif isinstance(piece, Piece.Reporter):
                        node.values[i] += 9
                else:
                    for j in range(len(Game.PLAYERS)):
                        otherPlayer = Game.PLAYERS[j]
                        if player is not otherPlayer:
                            if isinstance(piece, Piece.Militants):
                                node.values[j] += 1
                            elif isinstance(piece, Piece.Diplomat):
                                node.values[j] += 2
                            elif isinstance(piece, Piece.Necromobile):
                                node.values[j] += 2
                            elif isinstance(piece, Piece.Assassin):
                                node.values[j] += 3
                            elif isinstance(piece, Piece.Reporter):
                                node.values[j] += 3
                

    def doMove(self, number):
        move = int(number)
        print(self.root.children[move].move.piece.__class__.__name__, self.root.children[move].move.tileFrom.x, self.root.children[move].move.tileFrom.y, self.root.children[move].move.tile.x, self.root.children[move].move.tile.y)
        if self.root.children[move].move.bodyMoves:
            print(self.root.children[move].move.bodyMoves.tile.x, self.root.children[move].move.bodyMoves.tile.y)
        self.root.children[move].move.execute()
        Game.draw()
    
    def undoMove(self, number):
        move = int(number)
        print(self.root.children[move].move.piece.__class__.__name__, self.root.children[move].move.tile.x, self.root.children[move].move.tile.y)
        self.root.children[move].move.undo()
        Game.draw()