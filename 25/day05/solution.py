#!python3

with open('input.txt') as file:
    input_str = file.read()

database_str, ingredients_str = input_str.split('\n\n')

ingredients = [ int(s) for s in ingredients_str.splitlines() ]

database = [
    [ int(s) for s in line.split('-') ]
    for line in database_str.splitlines()
]

database.sort()

last = database.pop(0)
optimized = [last]

while database:
    item = database.pop(0)

    if item[0] <= last[1] + 1:
        if item[1] > last[1]:
            last[1] = item[1]
    else:
        optimized.append(item)
        last = item

all_fresh = 0
select_fresh = 0

for lo, hi in optimized:
    all_fresh += hi - lo + 1

for ingredient in ingredients:
    for lo, hi in optimized:
        if lo <= ingredient <= hi:
            select_fresh += 1
            break

print(f'Select fresh: {select_fresh}')
print(f'All fresh: {all_fresh}')
