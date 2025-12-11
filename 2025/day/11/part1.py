from sys import stdin

# input devices
graph = dict()

for line in stdin:
    devices = line.rstrip().split(' ')
    graph[devices[0].strip(':')] = devices[1:]


def dfs(current):
    paths = 0

    for device in graph[current]:
        if device == 'out':
            paths += 1
        else:
            paths += dfs(device)

    return paths

# count paths
paths = dfs('you')
print(paths)
