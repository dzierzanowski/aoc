#!python3
import re

with open('input.txt') as file:
    input_str = file.read()

pointer = 50
code = 0
input_str = input_str.replace('R', '').replace('L', '-')

for line in input_str.split('\n'):
    pointer += int(line)
    pointer %= 100
    if not pointer:
        code += 1

print(f'Code: {code}')
