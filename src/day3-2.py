import re
import os

day=3
if not os.path.exists(f"data/day{day}"):
    os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/day{day}", "r")
commands = re.findall("(do\(\)|mul\((\d|\d\d|\d\d\d),(\d|\d\d|\d\d\d)\)|don't\(\))", handle.read())
handle.close()

do_flag = True
sum = 0
for command in commands:
    if command[0] == "do()":
        do_flag = True
    elif command[0] == "don't()":
        do_flag = False
    elif do_flag:
        sum += int(command[1]) * int(command[2])

print(sum)
