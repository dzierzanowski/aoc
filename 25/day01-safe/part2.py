#!python3
import re

with open('input.txt') as file:
    input_str = file.read()

pointer = 50
code = 0
input_str = input_str.replace('R', '').replace('L', '-')

for line in input_str.split('\n'):
    i = int(line)
    val = abs(i)
    sign = i / val

    # full rotations
    full_rotations = int(val / 100)
    code += full_rotations
    val -= full_rotations * 100
    i = val * sign

    # once we counted full rotations, if the pointer is at zero
    # then it cannot pass zero again
    was_zero = pointer == 0
    pointer += i
    if not was_zero and pointer <= 0 or pointer >= 100:
        code += 1
    pointer %= 100

print(f'Code: {code}')
