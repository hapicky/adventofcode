from sys import stdin

ans = 0
for line in stdin:
    win_numbers = list(map(int, line.split('|')[0].split(':')[1].split()))
    numbers = list(map(int, line.split('|')[1].split()))
    wins = sum([n in win_numbers for n in numbers])

    if wins > 0:
        ans += pow(2, wins-1)

print(ans)
