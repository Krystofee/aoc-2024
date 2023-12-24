import re
from collections import defaultdict
from itertools import chain

with open('in.2.txt', 'r') as f:
    lines = f.readlines()

r_red = re.compile(r'(\d+) red([,;] )?')
r_green = re.compile(r'(\d+) green([,;] )?')
r_blue = re.compile(r'(\d+) blue([,;] )?')

possible = {
    r_red: 12,
    r_green: 13,
    r_blue: 14
}

def get_game_maxes(g):
    maxes = defaultdict(int)
    while len(g) > 0:
        for r, v in possible.items():
            m = r.match(g)
            if m:
                c = int(m.group(1))
                if c > maxes[r]:
                    maxes[r] = c
                g = g[m.span()[1]:].strip()
    return maxes


def get_maxes_max(m1, m2):
    m = defaultdict(int)
    for k in set(chain(m1.keys(), m2.keys())):
        m[k] = max(m1[k], m2[k])
    return m


total = 0

for i, l in enumerate(lines, start=1):
    l = l.replace(f'Game {i}: ', '')

    maxes = defaultdict(int)
    for g in l.split('; '):
        maxes = get_maxes_max(maxes, get_game_maxes(g))

    mulset = 1
    for v in maxes.values():
        mulset *= v

    total += mulset

    print(f'Game {i}:', mulset, maxes)

print(total)


