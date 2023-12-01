from sys import stdin

ans = 0
for line in stdin:
    l = None
    r = None

    for offset in range(len(line)):
        lc = line[offset]
        if l is None and lc.isnumeric():
            l = int(lc)
        
        rc = line[-(offset+1)]
        if r is None and rc.isnumeric():
            r = int(rc)
        
        if l is not None and r is not None:
            ans += l * 10 + r
            break

print(ans)
