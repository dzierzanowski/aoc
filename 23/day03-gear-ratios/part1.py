#!python3
import math, re

with open('input.txt') as file:
    input_str = file.read()

width = input_str.index('\n') + 1

re_symbol = re.compile(r'[^\d\.\n]')
re_number = re.compile(r'\d+')

symbols = set()
numbers = []

for match in re_symbol.finditer(input_str):
    symbol = match[0]
    i = match.start()
    x = i % width
    y = int(i / width)
    symbols.add((x, y))

for match in re_number.finditer(input_str):
    number = match[0]
    i = match.start()
    j = match.end()
    x_s = i % width - 1
    x_e = j % width
    y_s = int(i / width) - 1
    y_e = int(i / width) + 1
    for sym_x, sym_y in symbols:
        if x_s <= sym_x <= x_e and y_s <= sym_y <= y_e:
            numbers += [int(number)]
            break

print(f'Sum: {sum(numbers)}')
