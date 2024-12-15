from sys import stdin

ROBOT = '@'
WALL = '#'
BOX = 'O'
BOX_LEFT = '['
BOX_RIGHT = ']'
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
    org_len = len(row)

    # twice as wide
    row.extend([None] * org_len)
    for i in range(org_len - 1, -1, -1):
        if row[i] == WALL:
            row[i*2] = WALL
            row[i*2+1] = WALL
        elif row[i] == BOX:
            row[i*2] = BOX_LEFT
            row[i*2+1] = BOX_RIGHT
        elif row[i] == ROBOT:
            row[i*2] = ROBOT
            row[i*2+1] = SPACE
            sx = i*2
            sy = y
        else:
            row[i*2] = SPACE
            row[i*2+1] = SPACE

    rows.append(row)


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
    if dir == '<' or dir == '>':
        gx = nx + dx
        gy = ny

        # find next space position
        while True:
            if rows[gy][gx] == WALL:
                return (x, y)

            if rows[gy][gx] == SPACE:
                break
        
            gx += dx

        # move boxes
        for bx in range(gx, nx, -dx):
            rows[gy][bx] = rows[gy][bx - dx]

        rows[ny][nx] = SPACE
        return (nx, ny)

    else:
        # x to be moved
        move_x_at_y = [set() for _ in range(len(rows))]
        move_x_at_y[ny].add(nx)

        box_left_side = rows[ny][nx] == BOX_LEFT
        if box_left_side:
            move_x_at_y[ny].add(nx + 1)
        else:
            move_x_at_y[ny].add(nx - 1)
        
        gx = nx
        gy = ny + dy

        # find x to be moved
        while True:
            for gx in move_x_at_y[gy - dy]:
                if rows[gy][gx] == WALL:
                    return (x, y)
                
                if rows[gy][gx] == BOX_LEFT:
                    move_x_at_y[gy].add(gx)
                    move_x_at_y[gy].add(gx + 1)

                if rows[gy][gx] == BOX_RIGHT:
                    move_x_at_y[gy].add(gx)
                    move_x_at_y[gy].add(gx - 1)
            
            if len(move_x_at_y[gy]) == 0:
                # next all y positions are space
                break
        
            gy += dy

        # move boxes
        for by in range(gy, ny, -dy):
            for bx in move_x_at_y[by - dy]:
                rows[by][bx] = rows[by - dy][bx]
                rows[by - dy][bx] = SPACE

        if box_left_side:
            rows[ny][nx] = SPACE
            rows[ny][nx + 1] = SPACE
        else:
            rows[ny][nx] = SPACE
            rows[ny][nx - 1] = SPACE

        return (nx, ny)


# move
x = sx
y = sy
for i in range(len(moves)):
    x, y = move(x, y, moves[i])

# calculate GPS coordinates
ans = 0
for y, row in enumerate(rows):
    for x in range(len(row)):
        if row[x] == BOX_LEFT:
            ans += 100 * y + x

print(ans)
