#!python3
import math

with open('input.txt') as file:
    input_str = file.read()

time_str, record_str = input_str.split('\n')

times   = time_str.split()[1:]
times   += [ ''.join(times) ]
records = record_str.split()[1:]
records += [ ''.join(records) ]

results = []

for i in range(len(times)):
    time   = int(times[i])
    record = int(records[i])
    count  = 0
    for speed in range(1, time):
        duration = time - speed
        distance = duration * speed
        if distance > record:
            count += 1
    results += [ count ]

results_first  = math.prod(results[:-1])
results_second = results[-1]

print(f'Results first:  {results_first}')
print(f'Results second: {results_second}')
