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
    
    nex_value = sum([h[-1] for h in histories])
    ans += nex_value

print(ans)
