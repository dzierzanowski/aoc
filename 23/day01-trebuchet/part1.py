#!python3
import re

with open('input.txt') as file:
    input_str = file.read()

re_first = re.compile(r'^\D*(\d)')
re_last  = re.compile(r'(\d)\D*$')

params = []

for line in input_str.split('\n'):
    first = re_first.search(line).group(1)
    last  = re_last.search(line).group(1)
    params.append(int(first + last))

print(f'Sum: {sum(params)}')
