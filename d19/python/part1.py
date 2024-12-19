from functools import cache


@cache
def find_patterns(patterns, design):
    found_patterns_start = []
    found_patterns_end = []
    count = 0
    for p in patterns:
        if p == design:
            return 1
        if design.startswith(p):
            found_patterns_start.append(p)
        if design.endswith(p):
            found_patterns_end.append(p)
    for fp in found_patterns_start:
        if find_patterns(
            patterns,
            design[len(fp) :],
        ):
            count += 1
            break
    for fp in found_patterns_end:
        if find_patterns(
            patterns,
            design[: len(design) - len(fp)],
        ):
            count += 1
            break
    return count


with open("../input", "r") as file:
    patterns = tuple(file.readline().strip().split(", "))
    file.readline()
    count = 0
    for line in file.readlines():
        if line == "":
            continue
        print(f"Checking {line.strip()}")
        if find_patterns(patterns, line.strip()):
            count += 1
    print(count)
