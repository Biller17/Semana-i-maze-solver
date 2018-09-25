import fileinput
import re

import time

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

#print(labyrinth)

end_time = time.time()
print(end_time - start_time)