#!python3

with open('input.txt') as file:
    input_str = file.read()

seed_def, *map_defs = input_str.split('\n\n')

seeds = [ int(seed) for seed in seed_def.split()[1:] ]

maps = []

for map_def in map_defs:
    maps.append([
        {
            'range': range(int(src), int(src) + int(rng)),
            'dst': int(dst)
        }
        for dst, src, rng in [
            line.split() for line in map_def.split('\n')[1:]
        ]
    ])

locs = {}

for seed in seeds:
    transitional = seed
    for m in maps:
        for entry in m:
            if transitional in entry['range']:
                delta = transitional - entry['range'].start
                transitional = entry['dst'] + delta
                break
    locs[seed] = transitional

print(f'Lowest loc: {min(locs.values())}')
