import re

with open('in.1.txt', 'r') as f:
    lines = f.readlines()

r_red = re.compile(r'(\d+) red([,;] )?')
r_green = re.compile(r'(\d+) green([,;] )?')
r_blue = re.compile(r'(\d+) blue([,;] )?')

possible = {
    r_red: 12,
    r_green: 13,
    r_blue: 14
}

def is_game_possible(g):
    while len(g) > 0:
        for r, v in possible.items():
            m = r.match(g)
            if m:
                c = int(m.group(1))
                if c > v:
                    print(g, r, v, c)
                    return False
                g = g[m.span()[1]:].strip()
    return True

total = 0
total_impossible = 0

for i, l in enumerate(lines, start=1):
    total += i

    l = l.replace(f'Game {i}: ', '')

    for g in l.split('; '):
        if not is_game_possible(g):
            print(f"Game {i}: is impossible")
            total_impossible += i
            break

print(total, total_impossible, total - total_impossible)


