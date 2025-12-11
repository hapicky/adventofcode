from collections import defaultdict, deque
from sys import stdin

# input devices
graph = defaultdict(list)
in_deg = defaultdict(int)
all_devices = set()

for line in stdin:
    devices = line.rstrip().split(' ')
    start = devices[0].strip(':')
    graph[start] = devices[1:]

    for device in devices[1:]:
        in_deg[device] += 1

    all_devices.add(start)
    all_devices.update(devices[1:])


# topological sort
q = deque([device for device in all_devices if in_deg[device] == 0])
topo = []

while q:
    u = q.popleft()
    topo.append(u)

    for v in graph[u]:
        in_deg[v] -= 1
        if in_deg[v] == 0:
            q.append(v)


# count paths from
def count_paths(start):
    dp = defaultdict(int)
    dp[start] = 1

    for u in topo:
        for v in graph[u]:
            dp[v] += dp[u]
    
    return dp

paths_svr = count_paths('svr')
paths_fft = count_paths('fft')
paths_dac = count_paths('dac')

# svr -> fft -> dac -> out
# (dac -> fft is 0)
paths = paths_svr['fft'] * paths_fft['dac'] * paths_dac['out']
print(paths)
