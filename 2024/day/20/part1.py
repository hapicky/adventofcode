from sys import stdin
from copy import deepcopy
import heapq

# fastest time
fastest_times = []

# input map
rows = []

sx = None
sy = None
ex = None
ey = None

for y, line in enumerate(stdin):
    row = list(line.rstrip('\n'))
    rows.append(row)

    if 'S' in row:
        sx = row.index('S')
        sy = y

    if 'E' in row:
        ex = row.index('E')
        ey = y

    # init fastest time
    fastest_time = [float('inf')] * len(row)
    for x in range(len(row)):
        if row[x] == '#':
            fastest_time[x] = -1
    
    fastest_times.append(fastest_time)

# map size
H = len(rows)
W = len(rows[0])

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

# queue
q = None

def visit(fastest_times, cur_time, x, y):
    if fastest_times[y][x] > cur_time:
        fastest_times[y][x] = cur_time
    else:
        return
    
    if x == ex and y == ey:
        return

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        heapq.heappush(q, (cur_time + 1, nx, ny))

def update_fastest_times(initial_times, cur_step, sx, sy):
    global q
    q = []
    heapq.heappush(q, (cur_step, sx, sy))

    while len(q) > 0:
        step, x, y = heapq.heappop(q)
        visit(initial_times, step, x, y)


# no cheat fastest time
update_fastest_times(fastest_times, 0, sx, sy)
no_cheat_time = fastest_times[ey][ex]

# iterate cheat points
ans = 0

for cy in range(1, H - 1):
    for cx in range(1, W - 1):
        if rows[cy][cx] != '#':
            continue

        # iterate neighbor points
        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy

            if rows[ny][nx] == '#':
                continue

            # calcurate cheat time
            cheat_times = deepcopy(fastest_times)
            cheat_times[cy][cx] = float('inf')
            update_fastest_times(cheat_times, cheat_times[ny][nx] + 1, cx, cy)
            cheat_time = cheat_times[ey][ex]

            if no_cheat_time > cheat_time:
                print('cheat', cx, cy, 'save', no_cheat_time - cheat_time, 'picosec')

            if no_cheat_time - cheat_time >= 100:
                ans += 1
                break

print('answer', ans)
