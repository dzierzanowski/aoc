#!python3

with open('input.txt') as file:
    input_str = file.read()

seed_def, *map_defs = input_str.split('\n\n')

seed_def = [ int(seed) for seed in seed_def.split()[1:] ]
seeds = []
while seed_def:
    start  = seed_def.pop(0)
    length = seed_def.pop(0)
    seeds += [ range(start, start + length) ]

maps = []

for map_def in map_defs:
    maps.append([
        {
            'range': range(int(src), int(src) + int(rng)),
            'delta': int(dst) - int(src)
        }
        for dst, src, rng in [
            line.split() for line in map_def.split('\n')[1:]
        ]
    ])

locs = []

transitive = seeds
for m in maps:
    new_transitive = []
    while transitive:
        r1 = transitive.pop(0)
        did_overlap = False
        for entry in m:
            r2      = entry['range']
            delta   = entry['delta']
            overlap = range(max(r1.start,r2.start), min(r1.stop,r2.stop))
            if overlap:
                remainder_lo = range(r1.start, overlap.start)
                if remainder_lo:
                    transitive += [remainder_lo]
                remainder_hi = range(overlap.stop, r1.stop)
                if remainder_hi:
                    transitive += [remainder_hi]
                # Translate overlapping range
                overlap    = range(overlap.start + delta, overlap.stop + delta)
                new_transitive += [ overlap ]
                did_overlap = True
                break
        if not did_overlap:
            new_transitive += [ r1 ]
    transitive = new_transitive

locs = [ r.start for r in transitive ]

print(f'Lowest loc: {min(locs)}')
