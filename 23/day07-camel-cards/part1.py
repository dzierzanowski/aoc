#!python3
import re

with open('input.txt') as file:
    input_str = file.read()

regexes = [
    re.compile(r'(.)\1{4}'),
    re.compile(r'(.)\1{3}'),
    re.compile(r'(.)\1{2}(.)\2{1}'),
    re.compile(r'(.)\1{2}'),
    re.compile(r'(.)\1{1}(.)\2{1}'),
    re.compile(r'(.)\1{1}'),
    re.compile(r'.{5}'),
]

strengths = list(reversed([ 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ]))

def sorting_function(hand_bid):
    hand, bid   = hand_bid
    hand_sorted = ''.join(reversed(sorted(hand)))
    print(f'hand: {hand}, sorted: {hand_sorted}')
    value = 0
    # Determine type and put first character of value according to strength
    for i in range(len(regexes)):
        if regexes[i].match(hand_sorted):
            value = str(len(regexes) - i)
            break
    return str(value) + hand

hands = []

for line in input_str.split('\n'):
    hand, bid = line.split()
    # Convert to alphabetically-strong chars
    hand = ''.join([
        chr(ord('a') + strengths.index(card)) for card in hand
    ])
    bid = int(bid)
    hands += [ (hand, bid) ]

hands = sorted(hands, key = sorting_function)

score = 0

for i in range(len(hands)):
    _, bid = hands[i]
    score += (i + 1) * bid
    print(f'Hand {_} gets score {(i + 1) * bid}')

print(f'Score: {score}')
