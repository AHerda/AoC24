import re
import os

day=4
os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/zad0{day*2-1}-0{day * 2}", "r")
rows = handle.read().split()
handle.close()

columns = []
diagonals = []

rowlen = len(rows[0])

for i in range(rowlen):
    offset = 0
    column = ""
    diagonalR = ""
    diagonalL = ""

    for row in rows:
        if i + offset == rowlen:
            diagonals.append(diagonalR)
            diagonalR = ""
        if rowlen - 1 - i - offset == -1:
            diagonals.append(diagonalL)
            diagonalL = ""
        column += row[i]
        diagonalR += row[(i + offset) % rowlen]
        diagonalL += row[(rowlen - 1 - i - offset + rowlen) % rowlen] 
        offset += 1
    columns.append(column)
    diagonals.append(diagonalR)
    diagonals.append(diagonalL)

count = 0

for lines in [rows, columns, diagonals]:
    for line in lines:
        count += len(re.findall("XMAS", line))
        count += len(re.findall("SAMX", line))

print(count)
