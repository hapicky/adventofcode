from sys import stdin

# input problems
rows = []
symbols = None
is_space = None

for line in stdin:
    row = line.rstrip('\n')

    if is_space is None:
        is_space = [True] * (len(row) + 1)

    if row[0] == '*' or row[0] == '+':
        symbols = row.split()
    else:
        rows.append(row)
        for i, c in enumerate(row):
            is_space[i] = is_space[i] and c == ' '

# solve problems
answers = [0 if sym == '+' else 1 for sym in symbols]

l = 0
for i, symbol in enumerate(symbols):
    # detect next separator position
    r = is_space.index(True, l)

    for j in range(l, r):
        number = ''
        for row in rows:
            number += row[j]

        if symbol == '+':
            answers[i] += int(number)
        else:
            answers[i] *= int(number)

    # move to next column
    l = r + 1

total = sum(answers)
print(total)
