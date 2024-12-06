import re
import os

day=3
if not os.path.exists(f"data/day{day}"):
    os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/day{day}", "r")
pairs = re.findall("mul\((\d|\d\d|\d\d\d),(\d|\d\d|\d\d\d)\)", handle.read())
handle.close()

print(sum(map(lambda pair: int(pair[0]) * int(pair[1]), pairs)))
