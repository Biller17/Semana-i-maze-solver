import fileinput
import re

lineno = 0
row = 0

for line in fileinput.input():
    if lineno == 0:
        size = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        size = list(map(int, size))
        labyrinth = [0] * size[1]
        for i in range(size[1]):
            labyrinth[i] = [0] * size[0]

    if lineno == 1:
        start = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        start = list(map(int, start))

    if lineno == 2:
        end = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        end = list(map(int, end))

    if lineno > 2:
        maze = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        mazerow = [int(x) for x in str(maze[0])]
        for i in range(size[0]):
            labyrinth[row][i] = mazerow[i]
        row += 1
    lineno += 1

print(labyrinth)