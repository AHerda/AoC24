import os
import multiprocessing

day = 6
if not os.path.exists(f"data/day{day}"):
    os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/day{day}", "r")
mapa = list(map(list, handle.read().split("\n")[:-1]))
handle.close()

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_iter = 0

start = False

for i, row in enumerate(mapa):
    for j, cell in enumerate(row):
        if cell == "^":
            start = (i, j)
            break
    if start:
        break

def walk(pos, mapa2):
    global dir_iter
    (di, dj) = dirs[dir_iter]
    (i, j) = pos
    if mapa2[i + di][j + dj] == '#':
        dir_iter = (dir_iter + 1) % 4
        (di, dj) = dirs[dir_iter]
    return (i + di, j + dj)


def sim():
    global dir_iter
    visited = [start]
    pos = start
    while pos[0] + dirs[dir_iter][0] in range(len(mapa)) and pos[1] + dirs[dir_iter][1] in range(len(mapa[0])):
        pos = walk(pos, mapa)
        if pos not in  visited:
            visited.append(pos)
    return visited

print(len(sim()))
