#!python3

with open('input.txt') as file:
    input_str = file.read()

scratchcards = {}

for i in range(len(input_str.split('\n'))):
    scratchcards[i + 1] = 1

for card in input_str.split('\n'):
    half1, half2 = card.split(': ')
    card_id    = int(half1.split()[1])
    card_count = scratchcards[card_id]
    winning, given = [ set(half.split()) for half in half2.split(' | ') ]
    if winning & given:
        amount = len(winning & given)
        for i in range(amount):
            scratchcards[card_id + 1 + i] += card_count

print(f'Total number of cards: {sum(scratchcards.values())}')
