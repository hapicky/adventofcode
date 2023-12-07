from sys import stdin
from collections import defaultdict

orders = {
    'A': 'm',
    'K': 'l',
    'Q': 'k',
    'T': 'j',
    '9': 'i',
    '8': 'h',
    '7': 'g',
    '6': 'f',
    '5': 'e',
    '4': 'd',
    '3': 'c', 
    '2': 'b',
    'J': 'a'
}

strengths = {
    (5,): 7,
    (1, 4): 6,
    (2, 3): 5,
    (1, 1, 3): 4,
    (1, 2, 2): 3,
    (1, 1, 1, 2): 2,
    (1, 1, 1, 1, 1): 1
}

def parse(line):
    hand, bid = line.split()

    d = defaultdict(int)
    order = ''
    joker = 0
    for c in hand:
        if c == 'J':
            # ジョーカーの場合は枚数だけ控えておく
            joker += 1
        else:
            d[c] += 1

        order += orders[c]

    pair = sorted(d.values())
    if pair:
        # ジョーカーを最も多いカードとしてカウント
        for j in range(joker):
            pair[-1] += 1
    else:
        # すべてジョーカー
        pair = [5]

    strength = strengths[tuple(pair)]

    return (strength, order, hand, int(bid))


hands = []
for line in stdin:
    hands.append(parse(line))
hands.sort()

ans = 0
for i, hand in enumerate(hands):
    rank = i + 1
    bid = hand[3]
    ans += rank * bid

print(ans)
