time = int(input().split(':')[1].replace(' ', ''))
distance = int(input().split(':')[1].replace(' ', ''))

min_t = 0
for t in range(1, time):
    d = (time - t) * t
    if d > distance:
        min_t = t
        break

max_t = time
for t_diff in range(time):
    t = time - t_diff
    d = (time - t) * t
    if d > distance:
        max_t = t
        break

ans = max_t - min_t + 1
print(ans)
