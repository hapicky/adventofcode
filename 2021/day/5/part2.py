from sys import stdin

M_X = 1000
M_Y = 1000

dia = [[0] * M_X for _ in range(M_Y)]

for line in stdin:
    f, t = line.split(' -> ')
    x1, y1 = map(int, f.split(','))
    x2, y2 = map(int, t.split(','))

    if y1 == y2:
        s = min(x1, x2)
        e = max(x1, x2)
        for x in range(s, e + 1):
            dia[y1][x] += 1
    elif x1 == x2:
        s = min(y1, y2)
        e = max(y1, y2)
        for y in range(s, e + 1):
            dia[y][x1] += 1
    else:
        if y1 < y2:
            s_y = y1
            e_y = y2
            s_x = x1
            e_x = x2
        else:
            s_y = y2
            e_y = y1
            s_x = x2
            e_x = x1
        
        if s_x > e_x:
            sign = -1
        else:
            sign = 1

        for i, y in enumerate(range(s_y, e_y + 1)):
            dia[y][s_x + sign * i] += 1

# for d in dia:
#     print(d)

points = 0
for d in dia:
    for c in d:
        if c >= 2:
            points += 1

print(points)