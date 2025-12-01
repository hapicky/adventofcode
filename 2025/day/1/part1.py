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

    nex %= DIAL
    if nex == 0:
        password += 1

    cur = nex

print(password)
