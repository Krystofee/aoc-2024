with open("in.2.txt") as file:
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

maybe_gears = []

for i, l in enumerate(lines):
    for j in range(llen):
        if l[j] == "*":
            maybe_gears.append((i, j))

print(maybe_gears)

nums = set()

offsets = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1),
]

for i, j in maybe_gears:
    maybe_gear_nums = set()
    matched_nums = 0
    for pi, pj in offsets:
        ri = i + pi
        rj = j + pj
        if ri < 0 or rj < 0 or ri >= llen or rj >= llen:
            continue
        if lines[ri][rj].isdigit():
            num, start, end = find_number(lines[ri], rj)
            maybe_gear_nums.add((num, ri, start, end))
    if len(maybe_gear_nums) == 2:
        nums |= maybe_gear_nums
        n1, n2 = list(maybe_gear_nums)
        print("total+=", n1, n2)
        total += n1[0] * n2[0]


print(nums)
print(total)

