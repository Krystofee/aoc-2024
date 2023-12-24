with open("in.1.txt", "r") as file:
    lines = file.readlines()

times = [int(''.join([str(x) for x in lines[0].split()[1:]]))]
records = [int(''.join([str(x) for x in lines[1].split()[1:]]))]

print(times, records)

total = 1

for t, r in zip(times, records):
    speed, remaining = 0, t

    ways = 0
    for i in range(t):
        travelled = speed * remaining
        if travelled > r:
            ways += 1
        speed += 1
        remaining -= 1

    print("ways:", ways)
    total *= ways

print(total)

