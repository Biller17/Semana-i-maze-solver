# To compile use python lectura.py < filename.txt

import fileinput
import re

lineno = 0
row = 0

for line in fileinput.input():
	#Saves labyrinth size in array of two numbers and creates matrix to store it
    if lineno == 0:
        size = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        size = list(map(int, size))
        labyrinth = [0] * size[1]
        for row in range(size[1]):
            labyrinth[row] = [0] * size[0]
    #Saves start location in array of two numbers
    if lineno == 1:
        start = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        start = list(map(int, start))
    #Saves end location in array of two numbers
    if lineno == 2:
        end = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        end = list(map(int, end))
    #Stores labyrinth data in matrix
    if lineno > 2:
        temp = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        mazerow = [int(x) for x in str(temp[0])]
        for column in range(size[0]):
            labyrinth[row][column] = mazerow[column]
        row += 1
    lineno += 1

print(labyrinth)