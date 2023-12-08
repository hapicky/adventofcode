from sys import stdin
from collections import defaultdict
from math import lcm

nodes = defaultdict(dict)
currents = []

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

    if k.endswith('A'):
        currents.append(k)

steps = [0] * len(currents)
for i, cur in enumerate(currents):
    step = 0
    cur = currents[i]
    while not cur.endswith('Z'):
        direction = directions[step % len(directions)]
        cur = nodes[cur][direction]
        step += 1
    
    steps[i] = step

ans = lcm(*steps)
print(ans)
