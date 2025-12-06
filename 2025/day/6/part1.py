from sys import stdin

# input problems
rows = []
symbols = None

for line in stdin:
    row = line.strip().split()

    if row[0] == '*' or row[0] == '+':
        symbols = row
    else:
        rows.append(row)

# solve problems
answers = list(map(int, rows[0]))

for i in range(1, len(rows)):
    for j in range(len(rows[0])):
        if symbols[j] == '+':
            answers[j] += int(rows[i][j])
        else:
            answers[j] *= int(rows[i][j])

total = sum(answers)
print(total)
