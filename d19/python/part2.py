from functools import cache


@cache
def find_patterns(patterns, design):
    print(f"Checking {design} with patterns {patterns}")
    found_patterns_start = []
    count = 0
    for p in patterns:
        if p == design:
            print(f"Found final pattern {p}")
            count += 1
        elif design.startswith(p):
            print(f"Found pattern {p} in design {design}")
            found_patterns_start.append(p)
    count += sum(
        find_patterns(patterns, design[len(fp) :]) for fp in found_patterns_start
    )
    return count


with open("../input", "r") as file:
    patterns = tuple(file.readline().strip().split(", "))
    file.readline()
    count = 0
    for line in file.readlines():
        if line == "":
            continue
        print(f"Checking {line.strip()}")
        c = find_patterns(patterns, line.strip())
        print(f"Found {c} patterns")
        count += c
        # count += find_patterns(patterns, line.strip())
    print(count)
