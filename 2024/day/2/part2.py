from sys import stdin

ans = 0

def is_safe_levels(levels):
    diff = levels[1] - levels[0]
    if diff == 0:
        return False
    elif abs(diff) > 3:
        return False

    increase = levels[1] > levels[0]

    for i in range(2, len(levels)):
        diff = levels[i] - levels[i-1]
        if diff == 0:
            return False
        elif abs(diff) > 3:
            return False
        else:
            if increase:
                if diff < 0:
                    return False
            else:
                if diff > 0:
                    return False

    return True


for line in stdin:
    org_levels = list(map(int, line.split()))

    if is_safe_levels(org_levels):
        ans += 1
        continue

    for remove in range(len(org_levels)):
        levels = org_levels.copy()
        del levels[remove]

        if is_safe_levels(levels):
            ans += 1
            break

print(ans)
