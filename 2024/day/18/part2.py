import heapq

# input corrupted locations
# SIZE = 7
# BYTES = 12
SIZE = 71
BYTES = 1024

corrupted = [[False] * SIZE for _ in range(SIZE)]

for _ in range(BYTES):
    line = input()
    x, y = map(int, line.split(','))
    corrupted[y][x] = True

# minimum steps
min_steps = None

# queue
q = None

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def visit(step, x, y):
    global min_steps
    if min_steps[y][x] > step:
        min_steps[y][x] = step
    else:
        return

    if x == SIZE - 1 and y == SIZE - 1:
        return
    
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= SIZE or ny >= SIZE:
            continue

        if corrupted[ny][nx]:
            continue

        heapq.heappush(q, (step + 1, nx, ny))

def find_min_steps():
    global min_steps
    global q

    min_steps = [[float('inf')] * SIZE for _ in range(SIZE)]
    q = []
    heapq.heappush(q, (0, 0, 0))

    while len(q) > 0:
        step, x, y = heapq.heappop(q)
        visit(step, x, y)

    return min_steps[-1][-1]


while True:
    line = input()
    x, y = map(int, line.split(','))
    corrupted[y][x] = True

    steps = find_min_steps()
    if steps == float('inf'):
        ans = str(x) + ',' + str(y)
        print(ans)
        break
