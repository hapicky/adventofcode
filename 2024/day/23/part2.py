from sys import stdin
from collections import defaultdict
import heapq

graph = defaultdict(set)
computers = set()

for line in stdin:
    comp1, comp2 = line.rstrip('\n').split('-')

    graph[comp1].add(comp2)
    graph[comp2].add(comp1)

    computers.add(comp1)
    computers.add(comp2)

# queue
q = []
for comp in computers:
    heapq.heappush(q, (1, (comp,)))

largest = None
seen = set()

while len(q) > 0:
    size, comps = heapq.heappop(q)

    comp1 = comps[0]
    for nex in graph[comp1]:
        connected = True
        for other in comps[1:]:
            if other not in graph[nex]:
                connected = False
                break
        
        if connected:
            largest = tuple(sorted(comps + (nex,)))
            if largest not in seen:
                seen.add(largest)
                heapq.heappush(q, (size+1, largest))

ans = ','.join(largest)
print(ans)
