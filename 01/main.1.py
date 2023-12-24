import re

with open("in.1.txt", "r") as f:
    lines = f.readlines()

r = re.compile(r"([^0-9]*)([0-9])(.*)([0-9])([^0-9]*)")
r2 = re.compile(r"([^0-9]*?)([0-9])([^0-9]*?)")

s = 0
for l in lines:
    if l:
        m = r.match(l)
        if not m:
            m = r2.match(l)
            d = int(m.groups()[1])
            s += d * 10 + d
        else:
            d1, d2 = int(m.groups()[1]), int(m.groups()[3])
            s += d1 * 10 + d2

print(s)
