
import time
from Game import Game
from Move import Move
from Node import Node
import Piece
import random

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
                node.chosen = node
            return (node.values, node)
        

        moveWasFound = False
        currentMoves = None
        tempPlayerId = playerId
        while True:
            
            for piece in node.player.pieces:
                currentMoves = (piece.movesAI())
                for move in currentMoves:
                    moveWasFound = True
                    move.piece.bodyPlacementMoves(move)
                    if move.bodyMoves:
                        for bodyMove in move.bodyMoves:
                            copyMove = Move(move.piece, move.tile, move.tileFrom)
                            copyMove.bodyMoves = bodyMove
                            node.children.append(Node(copyMove, (tempPlayerId+1)%4))
                    else:
                        node.children.append(Node(move, (tempPlayerId+1)%4))
                    break
                if moveWasFound:
                    break
            if currentMoves:
                break
            tempPlayerId += 1
            node.playerId = (tempPlayerId+1)%4
            node.player = Game.PLAYERS[node.playerId]
                
        best, bestNode = self.getMove(node.children[0], (playerId+1)%4, Game.HEURISTICS_UPPER_BOUND, depth+1)



        firstRun = True

        for i in range(0, len(node.player.pieces)):
            
            
            if best[playerId] >= bound or time.time() - Game.MOVE_START_TIME > Game.WAIT_TIME:
                if node.move:
                    node.move.undo()
                    bestNode.chosen = node
                return (best, bestNode)
            
            piece = node.player.pieces[i]
            currentMoves = (piece.movesAI())
            current = None
            for move in currentMoves:
                if firstRun or random.randint(0,100) < Game.DROP_RATE:
                    firstRun = False
                    continue
                move.piece.bodyPlacementMoves(move)
                if move.bodyMoves:
                    for bodyMove in move.bodyMoves:
                        copyMove = Move(move.piece, move.tile, move.tileFrom)
                        copyMove.bodyMoves = bodyMove
                        newNode = Node(copyMove, (playerId+1)%4)


                        node.children.append(newNode)
                        current, currentNode = self.getMove(newNode, (playerId+1)%4, Game.HEURISTICS_UPPER_BOUND - best[playerId], depth+1)
                        if current[playerId] > best[playerId]:
                            best = current
                            bestNode = currentNode
                else:
                    newNode = Node(move, (playerId+1)%4)
                    node.children.append(newNode)
                    current, currentNode = self.getMove(newNode, (playerId+1)%4, Game.HEURISTICS_UPPER_BOUND - best[playerId], depth+1)
                    if current[playerId] > best[playerId]:
                        best = current
                        bestNode = currentNode
        if node.move:
            node.move.undo()
            bestNode.chosen = node
        return (best, bestNode)
            
            
        
    


    def heuristics(self, node):
        numberOfSurvivors = 3
        for player in Game.PLAYERS:
            if player.isChiefDead():
                numberOfSurvivors -= 1
        for i in range(len(Game.PLAYERS)):
            player = Game.PLAYERS[i]
            for piece in player.pieces:
                if not piece.dead:
                    if isinstance(piece, Piece.Militants):
                        node.values[i] += 6
                    elif isinstance(piece, Piece.Diplomat):
                        node.values[i] += 12
                    elif isinstance(piece, Piece.Necromobile):
                        node.values[i] += 12
                    elif isinstance(piece, Piece.Assassin):
                        node.values[i] += 18
                    elif isinstance(piece, Piece.Reporter):
                        node.values[i] += 18
                    else:
                        node.values[i] += 30
                else:
                    for j in range(len(Game.PLAYERS)):
                        otherPlayer = Game.PLAYERS[j]
                        if player is not otherPlayer and not otherPlayer.isChiefDead():
                            if player.isChiefDead():
                                if isinstance(piece, Piece.Militants):
                                    node.values[j] += 6 // (numberOfSurvivors + 1)
                                elif isinstance(piece, Piece.Diplomat):
                                    node.values[j] += 12 // (numberOfSurvivors + 1)
                                elif isinstance(piece, Piece.Necromobile):
                                    node.values[j] += 12 // (numberOfSurvivors + 1)
                                elif isinstance(piece, Piece.Assassin):
                                    node.values[j] += 18 // (numberOfSurvivors + 1)
                                elif isinstance(piece, Piece.Reporter):
                                    node.values[j] += 18 // (numberOfSurvivors + 1)
                                else:
                                    node.values[j] += 30 // (numberOfSurvivors + 1)
                            else:
                                if isinstance(piece, Piece.Militants):
                                    node.values[j] += 6 // numberOfSurvivors
                                elif isinstance(piece, Piece.Diplomat):
                                    node.values[j] += 12 // numberOfSurvivors
                                elif isinstance(piece, Piece.Necromobile):
                                    node.values[j] += 12 // numberOfSurvivors
                                elif isinstance(piece, Piece.Assassin):
                                    node.values[j] += 18 // numberOfSurvivors
                                elif isinstance(piece, Piece.Reporter):
                                    node.values[j] += 18 // numberOfSurvivors
                                else:
                                    node.values[j] += 30 // numberOfSurvivors
        
                                
                

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