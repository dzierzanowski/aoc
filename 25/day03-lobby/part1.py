#!python3
import re

with open('input.txt') as file:
    input_str = file.read()

s = 0

for line in input_str.split('\n'):
    left, right = 0, 0
    line = list(line)

    left = max(line[:-1])
    # print(left)
    where = line.index(left)
    # print(where)

    right = max(line[where + 1:])

    # print(right)

    result = int(left + right)

    s += result

    # print(f"{result}")

print(f"Sum of joltage: {s}")
