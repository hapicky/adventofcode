from sys import stdin

# カードの数
cards = dict()

for i, line in enumerate(stdin):
    card = i + 1

    # 初出のカードなら1で初期化
    if not card in cards:
        cards[card] = 1

    win_numbers = list(map(int, line.split('|')[0].split(':')[1].split()))
    numbers = list(map(int, line.split('|')[1].split()))
    wins = sum([n in win_numbers for n in numbers])

    # 勝った分だけ先のカードの数を（コピーも含めた数だけ）増やす
    for j in range(wins):
        n_card = card + j + 1
        if not n_card in cards:
            cards[n_card] = 1
        
        cards[n_card] += cards[card]

print(sum(cards.values()))
