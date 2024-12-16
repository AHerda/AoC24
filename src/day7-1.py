import os

day = 7
if not os.path.exists(f"data/day{day}"):
    os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/day{day}", "r")
equations = list(map(lambda row: (int(row.split(":")[0]), list(map(int, row.split(":")[1][1:].split(" ")))), handle.read().split("\n")[:-1]))
handle.close()

# print(equations)


def test(equation):
    result = equation[0]
    numbers = equation[1]
    if len(numbers) == 0:
        if result == 0:
            return True
        else:
            return False
    return test((result / numbers[-1], numbers[:-1])) or test((result - numbers[-1], numbers[:-1]))


print(sum(map(lambda x: x[0], filter(test, equations.copy()))))
