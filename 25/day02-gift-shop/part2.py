#!python3
import re

with open('input.txt') as file:
    input_str = file.read()

s = 0

for line in input_str.split(','):
    low_str, hi_str = line.split('-')

    for div in [2, 3, 5]:
        if len(low_str) %
        if len(low_str) % 2:
            # Find the lowest number that has one more digit, which is 10^p
            p = len(low_str)
            low = pow(10, p)
            low_str = str(low)
        l = int(len(low_str) / 2)
        half = low_str[:l]
        if int(half) < int(low_str[l:]):
            half = str(int(half) + 1)
        while int(half + half) <= int(hi_str):
            # print(f"Found: {half + half}")
            s += int(half + half)
            half = str(int(half) + 1)

print(f"Result: {s}")
