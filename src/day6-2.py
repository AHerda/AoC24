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
dir = dirs[0]

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
    while mapa2[i + di][j + dj] == '#':
        dir_iter = (dir_iter + 1) % 4
        (di, dj) = dirs[dir_iter]
    (di, dj) = dirs[dir_iter]
    return (i + di, j + dj)

def sim(pos, mapa2):
    global dir_iter
    dir_iter = 0
    (i, j) = pos
    mapa2[i][j] = '#'
    visited_states = [(start, dir_iter)]
    pos = start
    while pos[0] + dirs[dir_iter][0] in range(len(mapa)) and pos[1] + dirs[dir_iter][1] in range(len(mapa[0])):
        pos = walk(pos, mapa2)
        if (pos, dir_iter) in visited_states:
            return 1
        else:
            visited_states.append((pos, dir_iter))
    return 0

def sim2():
    global dir_iter
    visited = [start]
    pos = start
    while pos[0] + dirs[dir_iter][0] in range(len(mapa)) and pos[1] + dirs[dir_iter][1] in range(len(mapa[0])):
        pos = walk(pos, mapa)
        if pos not in  visited:
            visited.append(pos)
    return visited

def sim3(pos):
    mapa2 = [row.copy() for row in mapa]
    return sim(pos, mapa2.copy())

result = 0
visited = sim2()
visited = list(filter(lambda x: x != start, visited))
print(len(visited))
pool = multiprocessing.Pool(20)
out = pool.map(sim3, visited)

# print(out)
print(sum(out))
