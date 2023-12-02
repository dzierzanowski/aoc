#!python3
import re

with open('input.txt') as file:
    input_str = file.read()

re_first = re.compile(r'^\D*?(\d|one|two|three|four|five|six|seven|eight|nine)')
re_last  = re.compile(r'(?s:.*)(\d|one|two|three|four|five|six|seven|eight|nine)\D*?$')  # (?s:.*) to force searching from the end

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
params = []

for line in input_str.split('\n'):
    first = re_first.search(line).group(1)
    last  = re_last.search(line).group(1)
    if first in digits:
        first = str(digits.index(first) + 1)
    if last in digits:
        last = str(digits.index(last) + 1)
    params.append(int(first + last))

print(f'Sum: {sum(params)}')
