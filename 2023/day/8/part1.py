from sys import stdin
from collections import defaultdict

nodes = defaultdict(dict)
cur = None

for i, line in enumerate(stdin):
    if i == 0:
        directions = list(line.rstrip())
        continue
    
    if i == 1:
        continue

    k = line.split(' = ')[0]
    l = line[7:10]
    r = line[12:15]

    nodes[k]['L'] = l
    nodes[k]['R'] = r
    if cur is None:
        cur = k

step = 0
while cur != 'ZZZ':
    direction = directions[step % len(directions)]
    cur = nodes[cur][direction]
    step += 1

print(step)
