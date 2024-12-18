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
min_steps = [[float('inf')] * SIZE for _ in range(SIZE)]

# queue
q = []
heapq.heappush(q, (0, 0, 0))

# find min steps
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def visit(step, x, y):
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


while len(q) > 0:
    step, x, y = heapq.heappop(q)
    visit(step, x, y)

ans = min_steps[-1][-1]
print(ans)
