disk_map = input()
blocks = []
is_file = True
id = 0

# blocks
for c in disk_map:
    space = int(c)
    if is_file:
        blocks.extend([id] * space)
        id += 1
    else:
        blocks.extend(['.'] * space)
    
    is_file = not is_file

l = 0
r = len(blocks) - 1
ans = 0

# checksum
while l <= r:
    if blocks[l] == '.':
        while blocks[r] == '.':
            r -= 1

        if l > r:
            break

        ans += l * blocks[r]
        l += 1
        r -= 1
    else:
        ans += l * blocks[l]
        l += 1

print(ans)
