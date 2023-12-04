#!python3

with open('input.txt') as file:
    input_str = file.read()

scores = []

for card in input_str.split('\n'):
    half1, half2 = card.split(': ')
    card_id = int(half1.split()[1])
    winning, given = [ set(half.split()) for half in half2.split(' | ') ]
    score = 0
    if winning & given:
        score = 2 ** ( len(winning & given) - 1 )
    scores += [ score ]

print(f'Sum of scores: {sum(scores)}')
