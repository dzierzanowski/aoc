#!python3

with open('input.txt') as file:
    input_str = file.read()

lines = []

for line in input_str.splitlines():
    lines.append(list(line))

w = len(lines[0])
h = len(lines)

step = 0
total = 0
count = -1 # non-zero for starters

while count:
    step += 1
    replacables = []
    for y in range(h):
        for x in range(w):
            if lines[y][x] == '.':
                continue
            neighbors = 0
            for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= w or ny >= h:
                    continue
                if lines[ny][nx] == '@':
                    neighbors += 1
            if neighbors < 4:
                replacables.append((y, x))
    count = len(replacables)
    total += count
    print(f'Step {step}: {count}')
    for y, x in replacables:
        lines[y][x] = '.'

print(f'Total: {total}')
