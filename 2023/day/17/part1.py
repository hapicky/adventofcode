from sys import stdin
import heapq

rows = []

for line in stdin:
    row = list(map(int, line.rstrip()))
    rows.append(row)

width = len(rows[0])
height = len(rows)

min_loss = [[float('inf')] * width for _ in range(height)]
min_loss[0][0] = 0
visited = [[False] * width for _ in range(height)]
visited[0][0] =True

q = []
heapq.heapify(q)

heapq.heappush(q, ((0, 1), (0, 0), 0, 'down', visited))
heapq.heappush(q, ((0, 2), (0, 0), 0, 'down', visited))
# heapq.heappush(q, ((0, 3), (0, 0), 0, 'down', visited))
heapq.heappush(q, ((1, 0), (0, 0), 0, 'right', visited))
heapq.heappush(q, ((2, 0), (0, 0), 0, 'right', visited))
# heapq.heappush(q, ((3, 0), (0, 0), 0, 'right', visited))

px_py = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0),
}

def visit(point_to, point_from, cur_loss, dir, visited):
    if dir == 'up':
        dx = 0
        dy = -1
        n = abs(point_from[1] - point_to[1])
        next_dirs = ['left', 'right']
    elif dir == 'down':
        dx = 0
        dy = 1
        n = abs(point_from[1] - point_to[1])
        next_dirs = ['left', 'right']
    elif dir == 'left':
        dx = -1
        dy = 0
        n = abs(point_from[0] - point_to[0])
        next_dirs = ['up', 'down']
    elif dir == 'right':
        dx = 1
        dy = 0
        n = abs(point_from[0] - point_to[0])
        next_dirs = ['up', 'down']
    
    loss = cur_loss
    for i in range(n):
        x = point_from[0] + dx * (i + 1)
        y = point_from[1] + dy * (i + 1)
        loss += rows[y][x]
    
    min_loss[y][x] = min(min_loss[y][x], loss)
    visited[point_to[0]][point_to[1]] = True

    for next_dir in next_dirs:
        px, py = px_py[next_dir]
        next_point_to = (point_to[0] + px, point_to[1] + py)
        for i in range(3):
            if next_point_to[0] < 0 or width <= next_point_to[0] or next_point_to[1] < 0 or height <= next_point_to[1]:
                continue

            if visited[next_point_to[0]][next_point_to[1]] == True:
                continue

            heapq.heappush(q, (next_point_to, point_to, loss, next_dir, visited))
            next_point_to = (next_point_to[0] + px, next_point_to[1] + py)

while len(q) > 0:
    point_to, point_from, cur_loss, dir, v = heapq.heappop(q)
    visit(point_to, point_from, cur_loss, dir, v)

for l in min_loss:
    print(l)


print(min_loss[height-1][width-1])
