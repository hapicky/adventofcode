from itertools import chain, combinations
from sys import stdin

def solve(line):
    parts = line.split()
    indicator = parts[0][1:-1]

    # parse buttons
    buttons = []
    for part in parts[1:-1]:
        button = tuple(map(int, part.strip('()').split(',')))
        buttons.append(button)

    # calculate fewest button presses
    for presses in range(1, len(buttons) + 1):
        for pressed in combinations(buttons, presses):
            toggled = list(chain.from_iterable(pressed))

            matched = True
            for i, diagram in enumerate(indicator):
                light_on = toggled.count(i) % 2 == 1

                if diagram == '.':
                    if light_on:
                        matched = False
                        break
                elif not light_on:
                    matched = False
                    break

            if matched:
                return len(pressed)

    return float('inf')


presses = 0
for line in stdin:
    presses += solve(line.rstrip())

print(presses)
