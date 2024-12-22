from sys import stdin
from collections import deque, defaultdict

def mix(value, sec_number):
    return value ^ sec_number

def prune(sec_number):
    return sec_number % 16777216

bananas_for_seq = defaultdict(int)

for line in stdin:
    sec_number = int(line.rstrip('\n'))

    prev_price = sec_number % 10
    changes = deque()
    first_occur = dict()

    for _ in range(2000):
        # operation#1
        value = sec_number * 64
        sec_number = mix(value, sec_number)
        sec_number = prune(sec_number)

        # operation#2
        value = sec_number // 32
        sec_number = mix(value, sec_number)
        sec_number = prune(sec_number)

        # operation#3
        value = sec_number * 2048
        sec_number = mix(value, sec_number)
        sec_number = prune(sec_number)

        price = sec_number % 10
        if prev_price is None:
            prev_price = price
            continue

        change = price - prev_price
        changes.append(change)

        if len(changes) == 5:
            changes.popleft()

        if len(changes) == 4:
            change_seq = tuple(changes)
            if change_seq not in first_occur:
                first_occur[change_seq] = price

        prev_price = price

    for k, v in first_occur.items():
        bananas_for_seq[k] += v


ans = max(bananas_for_seq.values())
print(ans)
