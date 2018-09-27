"""
Miguel Monterrubio Bandera A01022153
Adrián Biller Alcántara A01018940
Omar Sanseviero Güezmes A01021626
"""


import fileinput
import re
import queue
from collections import defaultdict


exit = None
visited = None
maze = None

def checkHeuristic(child):
    heuristic = 2*(abs(child[0] - exit[0]) + abs(child[1] - exit[1]))
    return heuristic

def getMove(currentNode, childPos):
    for elem in currentNode:
        if elem[1] == childPos:
            return elem[2]

#a* algorithm with heuristic of out of place numbers
def bfs():
    path = ''
    #this will be the queue array to check the nodes
    maze, start = readLabyrinth()
    root = maze[tuple(start)]
    pq = queue.PriorityQueue()
    pq.put((0, root))
    numberOfActions = 0
    while(not pq.empty()):
        currentNode = pq.get()[1]
        visited[currentNode[0][0]] = True
        #if current node does not have the answer then expand and create children with possible moves and add them to the queue
        if(list(currentNode[0][0]) != exit):
            for child in currentNode:
                if(len(child[1]) > 1):
                    if(not visited[child[1]]):
                        #print(child[1])
                        heuristic = checkHeuristic(child[1])
                        maze[child[1]].append([currentNode[0][0], getMove(currentNode, child[1])])
                        pq.put((heuristic, maze[child[1]]))
        else:
            solution = ''
            node = currentNode
            while (list(node[0]) != start):
                node = currentNode[-1]
                solution += node[-1]
                currentNode = maze[node[0]]
            print(solution[::-1])
            return
        numberOfActions+=1
    print("-")


def readLabyrinth():
    global exit
    global visited
    lineno = 0
    graph = defaultdict(list)
    visited = {}
    prevRow = []
    for line in fileinput.input():
        if lineno > 2:
            row = list(line)[:-1]
            for i, elem in enumerate(row):
                if elem == '0':
                    currentLine = lineno-3
                    visited[(i,currentLine)] = False
                    if currentLine > 0:
                        # Add current to previous row
                        if prevRow[i] == '0':
                            graph[(i, currentLine-1)].append([(i, currentLine-1), (i, currentLine), 'D'])
                            graph[(i, currentLine)].append([(i, currentLine), (i, currentLine-1), 'U'])
                    if i+1 < len(row):
                        if row[i+1] == '0':
                            graph[(i, currentLine)].append([(i, currentLine), (i+1, currentLine), 'R']) 
                            graph[(i+1, currentLine)].append([(i+1, currentLine), (i, currentLine), 'L'])
            prevRow = row
        elif lineno == 0:
            size = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            size = list(map(int, size))
        elif lineno == 1:
            start = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            start = list(map(int, start))
            start = [start[0], size[1]-start[1]-1]
        elif lineno == 2:
            end = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            exit = list(map(int, end))
            exit = [exit[0], size[1]-exit[1]-1]
        lineno += 1
    return graph, start


if __name__ == '__main__':
    bfs()