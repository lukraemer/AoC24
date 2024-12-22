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


times = 2000
with open("../input") as file:
    sum = 0
    for line in file.readlines():
        n0 = int(line.strip())
        n = n0
        for i in range(times):
            n = get_next_secret_n(n)
        sum += n
print(sum)
