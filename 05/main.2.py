from copy import copy

import portion as P

with open("in.1.txt", "r") as file:
    lines = file.readlines()

seeds_ran = [int(x) for x in lines[0].replace('seeds: ', '').strip().split()]
seeds_inteval = P.empty()

for i in range(0, len(seeds_ran), 2):
    seeds_inteval |= P.closedopen(seeds_ran[i], seeds_ran[i] + seeds_ran[i + 1])

layers = []
layer = []
for l in lines[2:]:
    if ":" in l:
        continue
    if l == "\n":
        layers.append(layer)
        layer = []
        continue
    layer.append(tuple(int(x) for x in l.strip().split()))

layers.append(layer)

def shift_interval(compound_interval, shift):
    return compound_interval.apply(lambda x: (x.left, x.lower + shift, x.upper + shift, x.right))

current_interval = copy(seeds_inteval)

for layer in layers:
    new_interval = P.empty()
    for l in layer:
        layer_interval = P.closedopen(l[1], l[1] + l[2])
        intersection = current_interval.intersection(layer_interval)
        current_interval -= layer_interval
        new_interval |= shift_interval(intersection, l[0] - l[1])
    current_interval = new_interval | current_interval

print(current_interval.lower)
