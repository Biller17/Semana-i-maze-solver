import fileinput
import re

import time

start_time = time.time()

lineno = 0
row = 0

for line in fileinput.input():
    if lineno > 2:
        maze = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        labyrinth[row] = [int(x) for x in str(maze[0])]
        row += 1
    else:
        if lineno == 0:
            size = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            print(size)
            size = list(map(int, size))
            labyrinth = [0] * size[1]
            for i in range(size[1]):
                labyrinth[i] = [0] * size[0]

        elif lineno == 1:
            start = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            start = list(map(int, start))

        elif lineno == 2:
            end = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            end = list(map(int, end))

    lineno += 1

print(labyrinth)

end = time.time()
print(end - start_time)