disk_map = input()
blocks = []
is_file = True
id = 0

# blocks
for c in disk_map:
    space = int(c)
    if is_file:
        blocks.append((id, space))
        id += 1
    else:
        blocks.append(('.', space))

    is_file = not is_file

# move
r = len(blocks) - 1
while r > 0:
    if blocks[r][0] == '.':
        r -= 1
        continue

    l = 0
    id = blocks[r][0]
    size = blocks[r][1]
    while l < r:
        block = blocks[l]
        if block[0] == '.' and block[1] >= size:
            blocks[r] = ('.', size)
            blocks[l] = ('.', block[1] - size)
            blocks.insert(l, (id, size))
            break

        l += 1

    r -= 1

# checksum
l = 0
ans = 0

for block in blocks:
    if block[0] == '.':
        l += block[1]
    else:
        for _ in range(block[1]):
            ans += l * block[0]
            l += 1

print(ans)
