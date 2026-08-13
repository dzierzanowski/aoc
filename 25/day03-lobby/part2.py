#!python3
import re

with open('example.txt') as file:
    input_str = file.read()

s = 0

for line in input_str.split('\n'):

    top = ''
    line = list(line)
    last_idx = 0

    for i in reversed(range(2)):
        left = max(line[last_idx:-i])
        last_idx = line.index(left)
        top += left

    print(top)

    result = int(top)

    s += result

    # print(f"{result}")

# print(f"Sum of joltage: {s}")
