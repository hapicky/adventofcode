from sys import stdin

values = []
for line in stdin:
    depth = int(line)
    values.append(depth)

l = len(values)
sums = [0] * (l + 2)
for i in range(len(values)):
    sums[i] += values[i]
    sums[i + 1] += values[i]
    sums[i + 2] += values[i]

increased = 0
for i in range(3, l):
    if sums[i] > sums[i - 1]:
        increased += 1

print(increased)
