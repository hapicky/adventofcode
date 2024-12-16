from sys import stdin
import heapq

# min score needs to be kept per directions, y and x
# min_scores[direction][y][x]
min_scores = [list() for _ in range(4)]

# input map
rows = []
sx = None
sy = None
ex = None
ey = None

for y, line in enumerate(stdin):
    line = line.rstrip('\n')
    row = list(line)
    rows.append(row)

    if 'S' in row:
        sx = row.index('S')
        sy = y

    if 'E' in row:
        ex = row.index('E')
        ey = y

    # init min score
    for d in range(4):
        scores = [float('inf')] * len(row)
        for x in range(len(row)):
            if row[x] == '#':
                scores[x] = -1
        
        min_scores[d].append(scores)

for d in range(4):
    min_scores[d][sy][sx] = 0

directions = [
    (1, 0),     # East
    (0, 1),     # South
    (-1, 0),    # West
    (0, -1),    # North
]

# queue
q = []
heapq.heappush(q, (0, sx, sy, 0))

# Search for the minimum score
def visit(cur_score, x, y, d):
    for rotate in range(4):
        new_d = (d + rotate) % 4
        rotate_score = ((new_d - d) % 2) * 1000
        new_score = cur_score + rotate_score + 1

        dx, dy = directions[new_d]
        nx = x + dx
        ny = y + dy

        if new_score < min_scores[new_d][ny][nx]:
            min_scores[new_d][ny][nx] = new_score
            heapq.heappush(q, (new_score, nx, ny, new_d))

while len(q) > 0:
    cur_score, x, y, d = heapq.heappop(q)
    visit(cur_score, x, y, d)

ans = float('inf')
for d in range(4):
    ans = min(ans, min_scores[d][ey][ex])

print(ans)
