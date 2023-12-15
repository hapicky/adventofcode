def hash(label):
    value = 0
    for c in label:
        value += ord(c)
        value *= 17
        value %= 256
    
    return value

def lense_index(box, label):
    for i, lense in enumerate(box):
        if lense[0] == label:
            return i
    
    return -1


boxes = [list() for _ in range(256)]

steps = input().split(',')
for s in steps:
    if '-' in s:
        label = s.split('-')[0]
        h = hash(label)
        boxes[h] = [lense for lense in boxes[h] if lense[0] != label]

    if '=' in s:
        label, focal = s.split('=')
        h = hash(label)
        index = lense_index(boxes[h], label)
        if index < 0:
            boxes[h].append((label, focal))
        else:
            boxes[h][index] = (label, focal)


ans = 0
for box_i, box in enumerate(boxes):
    for lense_i, lense in enumerate(box):
        ans += (box_i + 1) * (lense_i + 1) * int(lense[1])
    
print(ans)
