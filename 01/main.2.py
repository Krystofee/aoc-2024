import re

with open("in.2.txt", "r") as f:
    lines = f.readlines()

digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

reversed_digits = {
    v: k for k, v in digits.items()
}

all_digits = {
    *digits.values(),
    *digits.keys(),
}

regexes = [
    re.compile(f".*?({x}).*?") for x in all_digits
]

def to_digit(s):
    if s not in all_digits:
        raise ValueError(f"Invalid digit: {s}")
    try:
        return int(s)
    except ValueError:
        return int(reversed_digits[s])

total = 0

for l in lines:
    if l:
        l = l.strip()
        ls, ld = 9999999, 0
        re, rd = -1, 0
        for r in regexes:
            for m in r.finditer(l):
                if m:
                    s, e = m.span(1)
                    if s < ls:
                        ls, ld = s, to_digit(m.groups()[0])
                    if e > re:
                        re, rd = e, to_digit(m.groups()[0])
        total += ld * 10 + rd

print(total)

