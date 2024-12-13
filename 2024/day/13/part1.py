from sys import stdin
import re

COST_A = 3
COST_B = 1

def play(a_x, a_y, b_x, b_y, p_x, p_y):
    token = float('inf')

    for a in range(min(p_x // a_x, p_y // a_y) + 1):
        for b in range(min(p_x // b_x, p_y // b_y) + 1):
            x = a_x * a + b_x * b
            y = a_y * a + b_y * b

            if x > p_x or y > p_y:
                break

            if x == p_x and y == p_y:
                token = min(token, a * COST_A + b * COST_B )

    if token == float('inf'):
        return 0
    else:
        return token


a_x = None
a_y = None
b_x = None
b_y = None
p_x = None
p_y = None

ans = 0

for line in stdin:
    line = line.rstrip('\n')

    if line.startswith('Button A'):
        parts = re.split(r'[\+,]', line)
        a_x = int(parts[1])
        a_y = int(parts[3])
    elif line.startswith('Button B'):
        parts = re.split(r'[\+,]', line)
        b_x = int(parts[1])
        b_y = int(parts[3])
    elif line.startswith('Prize'):
        parts = re.split(r'[=,]', line)
        p_x = int(parts[1])
        p_y = int(parts[3])
        token = play(a_x, a_y, b_x, b_y, p_x, p_y)
        ans += token

print(ans)
