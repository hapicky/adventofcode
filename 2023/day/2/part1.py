from sys import stdin

ans = 0
for line in stdin:
    id = int(line.split(':')[0].split()[1])
    possible = True

    parts = line.split(':')[1].split()
    for i, part in enumerate(parts):
        if part.startswith('red'):
            size = int(parts[i-1])
            if size > 12:
                possible = False
                break
        elif part.startswith('green'):
            size = int(parts[i-1])
            if size > 13:
                possible = False
                break
        elif part.startswith('blue'):
            size = int(parts[i-1])
            if size > 14:
                possible = False
                break
    
    if possible:
        ans += id

print(ans)
