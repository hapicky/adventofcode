from sys import stdin

ans = 0
for line in stdin:
    red = 0
    blue = 0
    green = 0

    parts = line.split(':')[1].split()
    for i, part in enumerate(parts):
        if part.startswith('red'):
            size = int(parts[i-1])
            red = max(red, size)
        elif part.startswith('green'):
            size = int(parts[i-1])
            green = max(green, size)
        elif part.startswith('blue'):
            size = int(parts[i-1])
            blue = max(blue, size)
    
    ans += red * blue * green

print(ans)
