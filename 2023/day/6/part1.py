import math

times = list(map(int, input().split(':')[1].split()))
distances = list(map(int, input().split(':')[1].split()))
ways = [0] * len(times)

for race in range(len(times)):
    way = 0
    for t in range(1, times[race]):
        d = (times[race] - t) * t
        if d > distances[race]:
            way += 1
    
    ways[race] = way

ans = math.prod(ways)
print(ans)
