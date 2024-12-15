from sys import stdin

ROBOT = '@'
WALL = '#'
BOX = 'O'
SPACE = '.'

# input map
rows = []
sx = None
sy = None

for y, line in enumerate(stdin):
    line = line.rstrip('\n')

    if line == '':
        break

    row = list(line)
    rows.append(row)

    if ROBOT in row:
        sx = row.index(ROBOT)
        sy = y

rows[sy][sx] = SPACE

# input moves
moves = []

for line in stdin:
    line = line.rstrip('\n')
    moves.extend(list(line))


directions = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0),
}

def move(x, y, dir):
    dx, dy = directions[dir]
    nx = x + dx
    ny = y + dy

    if rows[ny][nx] == WALL:
        return (x, y)
    
    if rows[ny][nx] == SPACE:
        return (nx, ny)

    # when next is BOX
    gx = nx + dx
    gy = ny + dy
    while rows[gy][gx] != WALL:
        if rows[gy][gx] == SPACE:
            rows[gy][gx] = BOX
            rows[ny][nx] = SPACE
            return (nx, ny)
    
        gx += dx
        gy += dy

    return (x, y)

# move
x = sx
y = sy
for i in range(len(moves)):
    x, y = move(x, y, moves[i])

# calculate GPS coordinates
ans = 0
for y, row in enumerate(rows):
    for x in range(len(row)):
        if row[x] == BOX:
            ans += 100 * y + x

print(ans)
