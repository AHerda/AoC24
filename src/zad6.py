import re
import os

day=3
os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/zad0{day*2-1}-0{day * 2}", "r")
commands = re.findall("(do\(\)|mul\((\d|\d\d|\d\d\d),(\d|\d\d|\d\d\d)\)|don't\(\))", handle.read())
handle.close()

print(commands)

do_flag = True
sum = 0
for command in commands:
    if command[0] == "do()":
        print("do")
        do_flag = True
    elif command[0] == "don't()":
        print("dont")
        do_flag = False
    elif do_flag:
        print(command[0])
        sum += int(command[1]) * int(command[2])
        print(sum)
    
