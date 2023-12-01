from sys import stdin

mappings = [
    {},
    {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    },
    {},
    {
        'one': 1,
        'two': 2,
        'six': 6
    },
    {
        'four': 4,
        'five': 5,
        'nine': 9
    },
    {
        'three': 3,
        'seven': 7,
        'eight': 8
    }
]

ans = 0
for line in stdin:
    l = None
    r = None

    for offset in range(len(line)):
        if l is None:
            for size, mapping in enumerate(mappings):
                ls = line[offset:(offset+size)]
                if ls in mapping:
                    l = mapping[ls]
                    break
        
        if r is None:
            for size, mapping in enumerate(mappings):
                # 末尾に改行文字があるのでさらに1文字左から始める
                s = len(line) - offset - size - 1
                e = s + size
                rs = line[s:e]
                if rs in mapping:
                    r = mapping[rs]
                    break

    ans += l * 10 + r

print(ans)
