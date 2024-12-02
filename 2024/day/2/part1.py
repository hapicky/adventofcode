from sys import stdin

ans = 0

for line in stdin:
    levels = list(map(int, line.split()))

    diff = levels[1] - levels[0]
    if diff == 0:
        continue
    elif abs(diff) > 3:
        continue

    increase = levels[1] > levels[0]
    safe = True

    for i in range(2, len(levels)):
        diff = levels[i] - levels[i-1]
        if diff == 0:
            safe = False
            break
        elif abs(diff) > 3:
            safe = False
            break
        else:
            if increase:
                if diff < 0:
                    safe = False
                    break
            else:
                if diff > 0:
                    safe = False
                    break

    if safe:
        ans += 1

print(ans)
