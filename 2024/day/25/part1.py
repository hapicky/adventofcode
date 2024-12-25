from sys import stdin

# input locks and keys
locks = []
keys = []
is_key = None
heights = None
ROWS = 8

for row, line in enumerate(stdin):
    line = line.rstrip('\n')

    # first line
    if row % ROWS == 0:
        is_key = line == '.....'
        heights = [0] * 5
        continue

    # last line
    if row % ROWS == ROWS - 2:
        if is_key:
            keys.append(heights)
        else:
            locks.append(heights)
        
        continue

    # count height
    for i, c in enumerate(line):
        if c == '#':
            heights[i] += 1


# try
ans = 0
for lock in locks:
    for key in keys:
        overlap = False
        for i in range(5):
            if lock[i] + key[i] > 5:
                overlap = True
                break
        
        if not overlap:
            ans += 1

print(ans)
