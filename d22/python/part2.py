from collections import defaultdict


def prune(n):
    return n % 16777216


def mix(secret_n, n):
    return secret_n ^ n


def get_next_secret_n(n):
    new_n = n * 64
    n = mix(n, new_n)
    n = prune(n)
    new_n = n // 32
    n = mix(n, new_n)
    n = prune(n)
    new_n = n * 2048
    n = mix(n, new_n)
    n = prune(n)
    return n


results = defaultdict(dict)
times = 2000
with open("../input") as file:
    for line in file.readlines():
        n_start = int(line.strip())
        n0 = n_start
        n1 = get_next_secret_n(n0)
        n2 = get_next_secret_n(n1)
        n3 = get_next_secret_n(n2)
        n = n3
        for i in range(times - 3):
            diff_1 = n1 % 10 - n0 % 10
            diff_2 = n2 % 10 - n1 % 10
            diff_3 = n3 % 10 - n2 % 10
            last_n = n
            n = get_next_secret_n(n)
            diff = n % 10 - last_n % 10
            if (diff_1, diff_2, diff_3, diff) not in results[n_start]:
                results[n_start][(diff_1, diff_2, diff_3, diff)] = int(str(n)[-1])
            n0 = n1
            n1 = n2
            n2 = n3
            n3 = n
    diffs = {}
    for key, value in results.items():
        for k, v in value.items():
            if k in diffs:
                diffs[k] = diffs[k] + v
            else:
                diffs[k] = v

    a = max(diffs, key=diffs.get)
    print(a)
    print(diffs[a])
