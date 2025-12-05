from sys import stdin

# input fresh ingredient ID ranges
fresh_ranges = []
for line in stdin:
    if line.rstrip() == '':
        break

    low, high = map(int, line.split('-'))
    fresh_ranges.append((low, high))


def is_fresh(id):
    return any(low <= id and id <= high for low, high in fresh_ranges)


# count fresh ingredient IDs
ans = 0
for line in stdin:
    id = int(line.rstrip())

    if is_fresh(id):
        ans += 1

print(ans)
