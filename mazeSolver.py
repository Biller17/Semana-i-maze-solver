"""
Miguel Monterrubio Bandera A01022153
Adrián Biller Alcántara A01018940
Omar Sanseviero Güezmes A01021626
"""


import fileinput
import re
import queue


#Node class for all nodes in the search tree
class Node:
    def __init__(self, position, maze, exit, moveDone, father):
        self.maze = maze
        self.position = position
        self.exit = exit
        self.moveDone = moveDone
        self.father = father
        self.childNodes = []
        self.heuristic = 0

    def checkHeuristic(self):
        heuristic = 2*(abs(self.position[0] - self.exit[0]) + abs(self.position[1] - self.exit[1]))
        self.heuristic = heuristic

    def __lt__(self,other):
        return (self.heuristic<other.heuristic)


    #returns an array of all possible moves in current zero position
    def checkPossibleMoves(self):
        posX  = self.position[0]
        posY = self.position[1]
        labyrinthSize = len(self.maze)-1
        moves = []
        #check Up
        # print("(", posX, ",", posY, ")")
        if((labyrinthSize - posY - 1) >= 0):
            if(self.maze[labyrinthSize-posY - 1][posX] == '0'):
                moves.append(["U",[posX, posY+1]])
            #up is possible
        #check Down
        if((labyrinthSize - posY + 1) <= labyrinthSize):
            if(self.maze[labyrinthSize-posY + 1][posX] == '0'):
                moves.append(["D", [posX, posY-1]])
        #check Right
        if(posX + 1 < len(self.maze[0])):
            if(self.maze[labyrinthSize - posY][posX + 1] == '0'):
                moves.append(["R",[posX+1, posY]])
        #check Left
        if(posX - 1 >= 0):
            if(self.maze[labyrinthSize - posY][posX - 1] == '0'):
                moves.append(["L",[posX-1, posY]])
        return moves

    def createChildren(self):
        possibleMoves = self.checkPossibleMoves()
        for i in range(len(possibleMoves)):
            self.childNodes.append(Node(possibleMoves[i][1], self.maze, self.exit, possibleMoves[i][0], self))
        return self.childNodes

#a* algorithm with heuristic of out of place numbers
def aStar():
    #this will be the queue array to check the nodes
    maze, start, exit = readLabyrinth()
    # print(start)
    visitedNodes = []
    foundExit = False
    root = Node(start, maze, exit ,"", None)

    pq = queue.PriorityQueue()
    pq.put((0, root))

    numberOfActions = 0
    while(not pq.empty()):
        currentNode = pq.get()[1]
        #if current node does not have the answer then expand and create children with possible moves and add them to the queue
        if(currentNode.position != exit):
            visitedNodes.append(currentNode.position)
            children = currentNode.createChildren()
            for i in range(len(children)):
                # print("child")
                if(children[i].position not in visitedNodes):
                    children[i].checkHeuristic()
                    pq.put((children[i].heuristic, children[i]))
        else:
            foundExit = True
            solution = ''
            while (currentNode.father != None):
                solution += currentNode.moveDone
                currentNode = currentNode.father
            return solution[::-1]
        numberOfActions+=1


def readLabyrinth():
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


if __name__ == '__main__':
    print("".join(aStar()))