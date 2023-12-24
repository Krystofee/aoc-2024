import portion as P


with open("in.2.txt", "r") as file:
    lines = file.readlines()

seeds_ran = [int(x) for x in lines[0].replace('seeds: ', '').strip().split()]


seeds = []
for i in range(0, len(seeds_ran), 2):
    seeds.append(P.closedopen(seeds_ran[i], seeds_ran[i] + seeds_ran[i + 1]))

print(seeds)

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

for l in layers:
    print(l)


def get_location(seed, layer):
    print("get_location", seed, layer)
    for l in layer:
        if l[1] <= seed < l[1] + l[2]:
            print("> match", l, seed, l[0] - l[1])
            return seed + l[0] - l[1]
    return seed


results = []


for seed in seeds:
    print(seed)
    for layer in layers:
        seed = get_location(seed, layer)
    results.append(seed)


print(results)
print(min(results))
