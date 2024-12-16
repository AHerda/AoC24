import os

day = 8
if not os.path.exists(f"data/day{day}"):
    os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/day{day}", "r")
rows = handle.read().split('\n')[:-1]
handle.close()

antennas = dict()
for i, row in enumerate(rows):
    for j, ch in  enumerate(row):
        if ch != '.':
            if ch in antennas.keys():
                antennas[ch].append((i, j))
            else:
                antennas[ch] = [(i, j)]

def diff(ant1, ant2):
    return (ant1[0] - ant2[0], ant1[1] - ant2[1])

def add(ant1, ant2):
    return (ant1[0] + ant2[0], ant1[1] + ant2[1])

def in_range(ant):
    return ant[0] in range(len(rows)) and ant[1] in range(len(rows[0]))

antinodes = []
for freq in antennas.keys():
    for i, antenna1 in enumerate(antennas[freq][:-1]):
        for antenna2 in antennas[freq][i + 1:]:
            antinode1 = add(antenna1, diff(antenna1, antenna2))
            antinode2 = add(antenna2, diff(antenna2, antenna1))
            if in_range(antinode1):
                antinodes.append(antinode1)
            if in_range(antinode2):
                antinodes.append(antinode2)

print(len(list(dict.fromkeys(antinodes))))
