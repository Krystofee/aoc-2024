with open("in.1.txt") as file:
    lines = []
    for l in file.readlines():
        lines.append(l.strip())

tlines = []
llen = len(lines[0])

for i in range(llen):
    tlines.append("")

for i, l in enumerate(lines):
    for j in range(llen):
        tlines[j] += l[j]

def print_lines(x):
    print("-"*llen)
    for l in x:
        print(l)
    print("-"*llen)


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def find_number(s, at):
    print("find_number", s, at)
    lat = at
    rat = at
    while True:
        if lat > 0 and is_int(s[lat - 1]):
            lat -= 1
        else:
            break
    while True:
        if rat < llen - 1 and is_int(s[rat + 1]):
            rat += 1
        else:
            break
    print(">>>", s, at, lat, rat, s[lat:rat + 1])
    return int(s[lat:rat + 1]), lat, rat + 1


total = 0

parts = []

for i, l in enumerate(lines):
    for j in range(llen):
        if l[j] != '.' and not l[j].isdigit():
            parts.append((i, j))

print(parts)

nums = set()

offsets = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1),
]

for i, j in parts:
    for pi, pj in offsets:
        ri = i + pi
        rj = j + pj
        if ri < 0 or rj < 0 or ri >= llen or rj >= llen:
            continue
        if lines[ri][rj].isdigit():
            num, start, end = find_number(lines[ri], rj)
            nums.add((num, ri, start, end))


print(nums)
print(sum(x[0] for x in nums))

