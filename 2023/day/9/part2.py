from sys import stdin

ans = 0
all_zero = {0}

for line in stdin:
    history = list(map(int, line.split()))
    histories = [history]

    while set(history) != all_zero:
        nex = [None] * (len(history) - 1)
        for i in range(len(history)-1):
            nex[i] = history[i+1] - history[i]
        
        histories.append(nex)
        history = nex

    left_value = 0
    for i in range(len(histories)-1):
        prev = len(histories) - 2 - i
        diff = histories[prev][0] - left_value
        left_value = diff

    ans += left_value

print(ans)
