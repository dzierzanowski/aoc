#!python3
import math, re

with open('input.txt') as file:
    input_str = file.read()

width = input_str.index('\n') + 1

re_symbol = re.compile(r'\*')
re_number = re.compile(r'\d+')

symbols = {}

for match in re_symbol.finditer(input_str):
    symbol = match[0]
    i = match.start()
    x = i % width
    y = int(i / width)
    # Key by gear coords, value is list of adjacent numbers
    symbols[(x, y)] = []

for match in re_number.finditer(input_str):
    number = match[0]
    i = match.start()
    j = match.end()
    x_s = i % width - 1
    x_e = j % width
    y_s = int(i / width) - 1
    y_e = int(i / width) + 1
    for symbol in symbols:
        sym_x, sym_y = symbol
        if x_s <= sym_x <= x_e and y_s <= sym_y <= y_e:
            symbols[symbol] += [int(number)]

result = sum([ math.prod(gear_values) for gear_values in symbols.values() if len(gear_values) == 2 ])

print(f'Result: {result}')
