from sys import stdin
from collections import defaultdict
from copy import deepcopy

# ブロック（キーはブロックの識別子、値は2つの三次元座標）
bricks = dict()
# ブロックID
brick_id = 1

# x, yの最大
max_x = 0
max_y = 0

# 入力
for line in stdin:
    f, t = line.rstrip().split('~')
    p1 = tuple(map(int, f.split(',')))
    p2 = tuple(map(int, t.split(',')))
    bricks[brick_id] = (p1, p2)
    brick_id += 1

    max_x = max(max_x, p1[0], p2[0])
    max_y = max(max_y, p1[1], p2[1])

# (x, y) における一番上のブロックを top_brick[y][x] とする（値はブロックID）
top_bricks = [[None for _ in range(max_x+1)] for _ in range(max_y+1)]

# 自分が支えているブロック
support_bricks = defaultdict(set)
# 自分が依存しているブロック
depend_bricks = defaultdict(set)

# zの小さい順に処理
for brick_id, (p1, p2) in sorted(bricks.items(), key=lambda i: i[1][0][2]):
    # 自分の下にあるブロックを探す
    below_bricks = set()
    for y in range(p1[1], p2[1]+1):
        for x in range(p1[0], p2[0]+1):
            if top_bricks[y][x] is not None:
                below_bricks.add(top_bricks[y][x])

    # 下のz座標を特定
    if below_bricks:
        below_z = max([bricks[b_id][1][2] for b_id in below_bricks])
        # 依存関係をメモ
        depends = set([b_id for b_id in below_bricks if bricks[b_id][1][2] == below_z])
        depend_bricks[brick_id] = depends
        for b_id in depends:
            support_bricks[b_id].add(brick_id)
    else:
        below_z = 0
    
    # 落下させた結果の新しいz座標に変更
    new_z1 = below_z + 1
    new_z2 = p2[2] - (p1[2] - new_z1)
    bricks[brick_id] = (
        tuple([p1[0], p1[1], new_z1]),
        tuple([p2[0], p2[1], new_z2]),
    )

    # ブロックのx, y範囲の一番上のブロックを更新
    for y in range(p1[1], p2[1]+1):
        for x in range(p1[0], p2[0]+1):
            top_bricks[y][x] = brick_id

# 集計
ans = 0
for brick_id in bricks.keys():
    # 依存関係をいじるのでコピーしておく
    depends = deepcopy(depend_bricks)

    # 落ちるブロックのIDと数（取り外すブロックは数えない）
    fall_ids = [brick_id]
    fall = 0

    while len(fall_ids) > 0:
        # 影響するブロックのID
        next_check_ids = set()

        for fall_id in fall_ids:
            for s_id in support_bricks[fall_id]:
                # 依存から落ちるブロックのIDを除去
                depends[s_id].discard(fall_id)
                next_check_ids.add(s_id)
        
        # 依存するブロックが0になってしまったら次のチェックに回してカウント
        fall_ids = [nid for nid in next_check_ids if len(depends[nid]) == 0]
        fall += len(fall_ids)
    
    ans += fall

print(ans)
