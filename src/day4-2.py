import re
import os

day=4
os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/zad0{day*2-1}-0{day * 2}", "r")
rows = handle.read().split()
handle.close()

count = 0
a = []

for i, row in enumerate(rows):
    for j, char in enumerate(row):
        if char == 'A':
            a.append((i, j))

for row, col in a:
    if row != 0 and col != 0 and row != len(rows[0]) - 1 and col != len(rows) - 1:
        ms = 0
        ss = 0
        for d1, d2 in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            if rows[row + d1][col + d2] == 'M':
                ms += 1
            elif rows[row + d1][col + d2] == 'S':
                ss += 1
            if ms == 2 and ss == 2 and rows[row + 1][col + 1] != rows[row - 1][col - 1]:
                count += 1

print(count)
