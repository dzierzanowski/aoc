#!python3

with open('input.txt') as file:
    input_str = file.read()

game_ids = []
limits = {
    'red':   12,
    'green': 13,
    'blue':  14,
}

for game in input_str.split('\n'):
    valid = True
    first, last = game.split(':')
    game_id = int(first.split(' ')[1])
    rounds = last.split(';')
    for r in rounds:
        draws = r.split(',')
        for draw in draws:
            number, color = draw[1:].split(' ')  # 1: to remove leading space
            if limits[color] < int(number):
                valid = False
                break
        if not valid:
            break
    if valid:
        game_ids += [ game_id ]

print(f'Sum: {sum(game_ids)}')
