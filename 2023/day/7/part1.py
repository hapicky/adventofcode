from sys import stdin
from collections import defaultdict

orders = {
    'A': 'm',
    'K': 'l', 
    'Q': 'k', 
    'J': 'j', 
    'T': 'i', 
    '9': 'h', 
    '8': 'g', 
    '7': 'f', 
    '6': 'e', 
    '5': 'd', 
    '4': 'c', 
    '3': 'b',  
    '2': 'a'
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
    for c in hand:
        d[c] += 1
        order += orders[c]

    pair = tuple(sorted(d.values()))
    strength = strengths[pair]

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
