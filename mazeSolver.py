import fileinput
import re

import time
import copy
import random
import time


#Node class for all nodes in the search tree
class Node:
    def __init__(self, position, maze, moveDone, father,isVisited):
        self.maze = maze
        self.position = position
        self.moveDone = moveDone
        self.isVisited = isVisited
        self.father = father
        self.childNodes = []
        self.heuristic = 0



    def printmaze(self):
        for i in range(len(self.maze)):
            print(self.maze[i])


    def checkHeuristic(self, finalBoard):
        heuristic = 0
        length = self.getAccumulatedPathWeight(0)
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if(self.maze[i][j] != finalBoard[i][j]):
                    heuristic += 1
        self.heuristic = heuristic + length
        # return heuristic


#returns an array of all possible moves in current zero position
    def checkPossibleMoves(self):
        posY, posX = self.getBlankPosition()
        moves = []
        #check Up
        if(posY -1 >= 0):
            moves.append("U")
            #up is possible
        #check Down
        if(posY +1 <= len(self.maze)-1):
            moves.append("D")
        #check Right
        if(posX +1 <= len(self.maze[0])-1):
            moves.append("R")
        #check Left
        if(posX -1 >= 0):
            moves.append("L")
        # print(moves)
        # self.createChildren(moves)
        return moves

#creates and returns an array of all the possible moves sent to the child nodes including the new board position
    def createChildren(self):
        possibleMoves = self.checkPossibleMoves()
        # print(possibleMoves)
        # print("possible moves",len(possibleMoves))
        for i in range(len(possibleMoves)):
            self.childNodes.append(Node(self.getNewBoard(possibleMoves[i]), possibleMoves[i],self, 0))
        return self.childNodes

        
#recursive function that returns all the moves done to reach the node with the solution
    def returnSolutionMove(self,moveset):
        # print(moveset)
        if(self.father == None):
            return moveset
        else:
            moveset.insert(0,self.moveDone)
            self.father.returnSolutionMove(moveset)
        return moveset

    def getAccumulatedPathWeight(self, length):
        if(self.father == None):
            return length
        else:
            self.father.getAccumulatedPathWeight(length + 1)
        return length




def checkIfVisited(node, nodeArray):
    for i in range(len(nodeArray)):
        if(node.maze == nodeArray[i].maze):
            return 1
    return 0



def prioritizeNodes(queue):
    quicksort(queue, 0, len(queue)-1)
    # for i in range(len(queue)):
    #     print("h:", queue[i].heuristic, end="")


def quicksort(array, left, right):
    if(left >= right):
        return 0
    pivot = array[ int((left + right) / 2)]
    index = partition(array, left, right, pivot)
    quicksort(array, left, index -1)
    quicksort(array, index, right)


def partition(array, left, right, pivot):
    while(left <= right):
        while(array[left].heuristic < pivot.heuristic ):
            left += 1
        while(array[right].heuristic > pivot.heuristic):
            right -= 1
        if(left <= right):
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
            right -= 1
    return left



#a* algorithm with heuristic of out of place numbers
def aStar():
    #this will be the queue array to check the nodes
    maze, start, exit = readLabyrinth()
    print(start)
    print(exit)
    queue = []
    visitedNodes = []
    foundExit = False
    root = Node(maze,"", None, 0)
    queue.insert(0, root)
    numberOfActions = 0
    while(foundExit != True):
        currentNode = queue.pop(0)
        print("board: ", numberOfActions)
        #if current node does not have the answer then expand and create children with possible moves and add them to the queue
        if(currentNode.maze != finalBoard):
            visitedNodes.append(currentNode)
            children = currentNode.createChildren()
            for i in range(len(children)):
                # print("child")
                # currentNode.printmaze()
                # print("\n")
                if(checkIfVisited(children[i], visitedNodes) == 0):
                    print(children[i].checkHeuristic(finalBoard))
                    queue.insert(0, children[i])
            prioritizeNodes(queue)
        else:
            foundExit = True

            print("Found Solution! ")
            return currentNode.returnSolutionMove([])

        numberOfActions+=1



def readLabyrinth():
    start_time = time.time()

    lineno = 0
    labyrinth = []
    for line in fileinput.input():
        if lineno > 2:
            labyrinth.append(list(line)[:-1])
        elif lineno == 1:
            start = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            start = list(map(int, start))

        elif lineno == 2:
            end = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            end = list(map(int, end))
        lineno += 1
    return labyrinth, start, end
#print(labyrinth)

    # end_time = time.time()
    # print(end_time - start_time)


if __name__ == '__main__':
    start_time = time.time()
    aStar(maze)
    print("El programa tomó %s segundos " % (time.time() - start_time))
