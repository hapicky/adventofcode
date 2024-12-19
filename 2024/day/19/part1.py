from sys import stdin
from functools import cache

# input patterns
patterns = input().split(', ')

@cache
def is_possible(design):
    if design in patterns:
        return True

    for pattern in patterns:
        l = len(pattern)
        head = design[:l]

        if head == pattern:
            rest = design[l:]
            if is_possible(rest):
                return True
    
    return False

ans = 0
for line in stdin:
    design = line.rstrip('\n')
    if design == '':
        continue

    if is_possible(design):
        ans += 1

print(ans)
