from sys import stdin
from collections import defaultdict

graph = defaultdict(set)
ans = 0

for line in stdin:
    comp1, comp2 = line.rstrip('\n').split('-')

    graph[comp1].add(comp2)
    graph[comp2].add(comp1)

    for comp3 in graph[comp1]:
        if comp3 == comp2:
            continue

        if comp2 not in graph[comp3]:
            continue

        if comp1[0] == 't' or comp2[0] == 't' or comp3[0] == 't':
            ans += 1

print(ans)
