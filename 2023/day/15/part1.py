steps = input().split(',')

ans = 0
for s in steps:
    value = 0

    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    
    ans += value

print(ans)
