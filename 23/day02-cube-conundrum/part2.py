#!python3
import math

with open('input.txt') as file:
    input_str = file.read()

power_sum = 0

for game in input_str.split('\n'):
    first, last = game.split(':')
    amount = {
        'red':   0,
        'green': 0,
        'blue':  0,
    }
    rounds = last.split(';')
    for r in rounds:
        draws = r.split(',')
        for draw in draws:
            number, color = draw[1:].split(' ')  # 1: to remove leading space
            amount[color] = max(amount[color], int(number))
    power_sum += math.prod(amount.values())

print(f'Powers: {power_sum}')
