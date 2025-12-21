from sys import stdin
import z3

def calc_fewest_presses(buttons, joltage):
    opt = z3.Optimize()

    # button press count
    presses = z3.IntVector('press', len(buttons))

    for press in presses:
        opt.add(press >= 0)

    # configured joltage
    _ = z3.IntVector('joltage', len(joltage))

    for joltage_i, requirement in enumerate(joltage):
        opt.add(z3.Sum([press for button_i, press in enumerate(presses) if joltage_i in buttons[button_i]]) == requirement)

    # fewest button presses
    opt.minimize(z3.Sum(presses))
    opt.check()
    m = opt.model()
    fewest_presses = m.evaluate(z3.Sum(presses))

    return fewest_presses.as_long()


# input manuals
manuals = []

for line in stdin:
    parts = line.rstrip().split()
    joltage = tuple(map(int, parts[-1][1:-1].split(',')))

    buttons = []
    for part in parts[1:-1]:
        button = tuple(map(int, part.strip('()').split(',')))
        buttons.append(button)

    manuals.append([buttons, joltage])


# calculate fewest button presses
ans = 0
for i, (buttons, joltage) in enumerate(manuals):
    presses = calc_fewest_presses(buttons, joltage)
    ans += presses

print(ans)
