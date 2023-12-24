import re

with open('in.1.txt', 'r') as file:
    lines = file.readlines()

r_card = re.compile('Card\s+\d+: ')

total = 0

for i, l in enumerate(lines, start=1):
    l = re.sub(r_card, '', l)
    a, b = l.split('|')
    winning = [int(x.strip()) for x in a.strip().split()]
    my = [int(x.strip()) for x in b.strip().split()]
    t = 0
    for w in winning:
        if w in my:
            if not t:
                t = 1
            else:
                t += t
    total += t

print(total)