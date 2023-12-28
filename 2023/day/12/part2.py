from sys import stdin

def count_arrangements(left, right):
    # print(left)
    # print(right)

    # 左からi文字目までが取りうる選択肢をdp[i]とする（値は文字列の配列）
    dp = [list() for _ in range(len(left)+1)]
    # 0文字目までは空文字一択
    dp[0].append('')

    for i in range(1, len(left)+1):
        # i文字目だけ考えた場合の選択肢
        if left[i-1] == '?':
            choices = ['.', '#']
        else:
            choices = [left[i-1]]

        for prev_str in dp[i-1]:
            for choice in choices:
                # 左までの選択肢にi文字目を足した文字列
                cur_str = prev_str + choice
                # これまでの文字列に「#」の塊がいくつあるか
                groups = [x for x in map(lambda x: len(x), cur_str.split('.')) if x > 0]

                # 右端まで来ていたら完全にあっている必要がある
                if i == len(left):
                    if groups == right:
                        dp[i].append(cur_str)

                    continue
                
                # 塊なしの場合は無条件で候補に追加する
                if len(groups) == 0:
                    dp[i].append(cur_str)
                    continue

                # 現在の文字が「#」の場合はまだ続く場合があるので右端を無視
                if choice == '#' and len(groups) <= len(right) and right[len(groups)-1] > groups[-1]:
                    groups.pop(-1)
                
                # 塊の数が一致すれば候補に追加
                if groups == right[0:len(groups)]:
                    dp[i].append(cur_str)

    #     print(i, dp[i])

    # print('---')

    return len(dp[-1])


COPIES = 5

ans = 0
for i, line in enumerate(stdin):
    l, r = line.rstrip().split()
    left = '?'.join([l] * COPIES)
    right = list(map(int, r.split(','))) * COPIES

    arrangements = count_arrangements(left, right)
    ans += arrangements
    # print(i+1, arrangements)

print(ans)
