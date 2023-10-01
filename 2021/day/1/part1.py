from sys import stdin

prev = float('inf')
increased = 0

for line in stdin:
    depth = int(line)
    if depth > prev:
        increased += 1
    
    prev = depth

print(increased)
