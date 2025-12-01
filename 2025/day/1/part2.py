from sys import stdin

cur = 50
password = 0
DIAL = 100

for line in stdin:
    d = line[0]
    v = int(line[1:])

    if line[0] == 'L':
        nex = cur - v
    elif line[0] == 'R':
        nex = cur + v

    count = 0
    if nex == 0:
        count = 1
    elif nex < 0:
        count = abs(nex) // DIAL
        if cur > 0:
            count += 1
    elif nex >= 100:
        count = nex // DIAL

    nex %= DIAL
    cur = nex
    password += count

print(password)
