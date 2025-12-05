from sys import stdin

def is_overlap(range1, range2):
    low1, high1 = range1
    low2, high2 = range2

    if low1 <= low2 and low2 <= high1:
        return True

    if low1 <= high2 and high2 <= high1:
        return True

    if low2 <= high1 and high1 <= high2:
        return True

    return False


def merge_ranges(ranges, new_range):
    new_ranges = ranges.copy()

    while True:
        merged = False
        for i, rng in enumerate(new_ranges):
            if is_overlap(rng, new_range):
                new_range = (min(rng[0], new_range[0]), max(rng[1], new_range[1]))
                del new_ranges[i]
                merged = True
                break

        if not merged:
            break

    new_ranges.append(new_range)
    return new_ranges


def main():
    # input fresh ingredient ID ranges
    fresh_ranges = []
    for line in stdin:
        if line.rstrip() == '':
            break

        low, high = map(int, line.split('-'))
        fresh_ranges = merge_ranges(fresh_ranges, (low, high))

    # count fresh ingredient IDs
    ans = 0
    for rng in fresh_ranges:
        ans += rng[1] - rng[0] + 1

    print(ans)


if __name__ == "__main__":
    main()
