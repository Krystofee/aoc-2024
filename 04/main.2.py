import re
from collections import defaultdict

with open('in.2.txt', 'r') as file:
    lines = file.readlines()

r_card = re.compile('Card\s+\d+: ')


def get_score(lw, lm):
    t = 0
    for w in lw:
        if w in lm:
            t += 1
    return t


def get_cards(i, lw, lm):
    result = defaultdict(int)
    s = get_score(lw, lm)
    for j in range(s):
        game_idx = i + j + 1
        result[game_idx] += 1
    return result


games = {}
games_count = defaultdict(int)

for i, l in enumerate(lines, start=1):
    l = re.sub(r_card, '', l)
    a, b = l.split('|')
    winning = tuple(int(x.strip()) for x in a.strip().split())
    my = tuple(int(x.strip()) for x in b.strip().split())
    games[i] = (winning, my)
    games_count[i] = 1

for i, g in games.items():
    new_cards = get_cards(i, g[0], g[1])
    for k, v in new_cards.items():
        games_count[k] += v * games_count[i]

print(sum(games_count.values()))
